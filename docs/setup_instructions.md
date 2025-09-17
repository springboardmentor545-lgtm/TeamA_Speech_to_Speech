# Setup Instructions – AI-Powered Speech Translation

## 1. Create Azure Speech Resource
1. Log in to [Azure Portal](https://portal.azure.com/).
2. Click **Create a Resource → Search "Speech Service" → Create**.
3. Fill details:
   - Subscription: Free Trial / Pay-As-You-Go
   - Resource Group: Create new (e.g., SpeechProj)
   - Region: Nearest to you (e.g., centralindia)
   - Name: speech-demo-1
   - Pricing Tier: Free (F0) if available
4. Click **Review + Create → Create**.
5. After deployment, go to the resource → **Keys and Endpoint** tab. Copy **Key 1** and note the **Region**.

## 2. Install Dependencies
Open your terminal and run:
```bash
pip install azure-cognitiveservices-speech
pip install python-dotenv   # optional, for environment variables
```
## 3. Configure Environment

Create a .env file in the root directory.

Add the following lines:
```bash
AZURE_SPEECH_KEY=your_speech_key
AZURE_REGION=centralindia
```
### 4. Run Sample Code

- Single File Recognition:

python src/recognize_once.py

Recognizes speech from a .wav file or live mic.

Saves transcription in results/transcriptions/.

- Continuous Microphone Recognition:
python src/continuous_recognition.py


Listens continuously and prints recognized text.

Optionally saves transcriptions automatically.

## Notes

Ensure .wav audio files are 16kHz, mono for best recognition.

Large files should be tracked using Git LFS.

You can add new languages by updating speech_config.speech_recognition_language.
