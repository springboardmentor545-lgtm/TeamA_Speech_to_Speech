import os
import json
from datetime import datetime

# Directory for storing results
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

FILES = {
    "hi-IN": os.path.join(RESULTS_DIR, "hindi_transcriptions.json"),
    "en-IN": os.path.join(RESULTS_DIR, "english_transcriptions.json"),
}

def _load_json(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def _save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_transcript(text, detected_lang):
    """Save transcript to the correct JSON file (English or Hindi)."""

    # Normalize language codes
    if detected_lang.startswith("en"):
        detected_lang = "en-IN"
    elif detected_lang.startswith("hi"):
        detected_lang = "hi-IN"
    else:
        return  # skip unsupported

    file_path = FILES[detected_lang]
    data = _load_json(file_path)

    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "text": text,
        "language": detected_lang,
    }
    data.append(entry)
    _save_json(file_path, data)

    print(f" Saved transcript to {os.path.basename(file_path)}")
