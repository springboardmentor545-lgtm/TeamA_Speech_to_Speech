from cgitb import text
import os
import time
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv
from db_json import save_transcript  # Use central JSON saver

# Load environment variables
load_dotenv()
speech_key = os.getenv("SPEECH_key")
speech_region = os.getenv("speech_region")

# ----------------- Core Recognizer -----------------
def recognize_once(audio_config):
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    auto_detect_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(
        languages=["en-IN", "hi-IN"]
    )

    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        auto_detect_source_language_config=auto_detect_config,
        audio_config=audio_config
    )

    result = recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech and result.text.strip():
        auto_detect_result = speechsdk.AutoDetectSourceLanguageResult(result)
        return auto_detect_result.language, result.text.strip()
    return None, None

# ----------------- Public APIs -----------------
def recognize_from_mic():
    print("🎤 Starting microphone recognition...")
    print("🎤 Speak into your microphone... (press Ctrl+C to stop)")
    try:
        while True:
            lang, text = recognize_once(speechsdk.audio.AudioConfig(use_default_microphone=True))
            if text:
                if lang == "en-IN":
                    print(f"[en-IN] {text}")
                    save_transcript(text, "en-IN")
                elif lang == "hi-IN":
                    print(f"[hi-IN] {text}")
                    save_transcript(text, "hi-IN")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n Stopped by user.")

def recognize_from_audio_file(file_path):
    if not os.path.exists(file_path):
        print(" File not found:", file_path)
        return

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=speech_region)
    auto_detect_config = speechsdk.languageconfig.AutoDetectSourceLanguageConfig(languages=["en-IN", "hi-IN"])
    audio_config = speechsdk.audio.AudioConfig(filename=file_path)

    recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config,
        auto_detect_source_language_config=auto_detect_config,
        audio_config=audio_config
    )

    done = False  # Flag to track when recognition is finished

    def recognized_cb(evt):
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech and evt.result.text.strip():
            auto_detect_result = speechsdk.AutoDetectSourceLanguageResult(evt.result)
            lang = auto_detect_result.language
            text = evt.result.text.strip()
            if lang == "en-IN":
                print(f"[en-IN] {text}")
                save_transcript(text, "en-IN")   # ✅ pass text + lang
            elif lang == "hi-IN":
                print(f"[hi-IN] {text}")
                save_transcript(text, "hi-IN")  # ✅ pass text + lang


    def stop_cb(evt):
        nonlocal done
        print("Finished processing audio file.")
        done = True

    recognizer.recognized.connect(recognized_cb)
    recognizer.session_stopped.connect(stop_cb)
    recognizer.canceled.connect(stop_cb)

    recognizer.start_continuous_recognition_async().get()

    # Wait until recognition is finished
    import time
    while not done:
        time.sleep(0.5)

    recognizer.stop_continuous_recognition_async().get()


