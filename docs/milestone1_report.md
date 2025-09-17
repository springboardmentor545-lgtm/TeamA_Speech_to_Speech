# Milestone 1 Report – Speech Recognition and Data Collection

## Objective
Collect live speech data and enable accurate speech recognition for multiple languages (English & Hindi).

## Steps Followed

### 1. Setup Azure Speech Service
- Created a Speech resource in Azure Portal.
- Copied Subscription Key and Region for SDK access.
- Installed Azure Speech SDK in Python:
```bash
pip install azure-cognitiveservices-speech
```
### 2. Data Collection
Recorded short audio clips (10–20 sec) in English and Hindi.

Stored files in structured folders:

data/

├── english/

├── hindi/

### 3. Speech Recognition

Tested single-file recognition with .wav samples.

Tested live microphone recognition.

Ensured recognition works for:

English (en-US)

Hindi (hi-IN)

## Dataset Details
- no.of audio files: 8

  engish: 4

  hindi: 4
- duration: 10-20 seconds each

- languages: english, hindi
## Challenges & Solutions

Unicode errors with Hindi text: Solved by using encoding='utf-8' while saving transcriptions.

Audio format issues: Ensured all files are .wav, 16kHz, mono.

Recognition accuracy: Tested multiple takes; short pauses in speech improved results.

## Conclusion

Speech recognition works reliably for English and Hindi.

Data collected is structured, documented, and ready for further processing.
