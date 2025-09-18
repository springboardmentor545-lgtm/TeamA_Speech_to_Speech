from speech_recognizer import recognize_from_mic, recognize_from_audio_file

def main():
    print("Choose input type:")
    print("1. Microphone")
    print("2. Audio file")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        recognize_from_mic()
    elif choice == "2":
        file_path = input("Enter audio file path: ").strip()
        recognize_from_audio_file(file_path)
    else:
        print(" Invalid choice.")

if __name__ == "__main__":
    main()
