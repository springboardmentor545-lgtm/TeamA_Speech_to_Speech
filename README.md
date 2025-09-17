# TeamA_Speech_to_Speech   

**Project Title:** 
AI-Powered Real-Time Speech Translation for Multilingual Content

**Description:** 
This project develops a real-time speech-to-speech translation system that converts live commentary or spoken content from English/Hindi into 12+ languages. It is designed to be embedded in OTT digital feeds, enhancing accessibility and providing a seamless multilingual viewing experience. The system uses Azure Speech-to-Text for speech recognition and Azure OpenAI for translation.

## Tech Stack
- **Python 3.x** – programming language  
- **Azure Cognitive Services** – Speech-to-Text for accurate speech recognition  
- **Azure OpenAI** – for multilingual translation  
- **Jupyter Notebooks** – testing and experimentation  
- **pandas & openpyxl** – handling transcription outputs  
- **pydub** – optional audio preprocessing 

## Team Members
- Arunkumar  
- Chindam Manyasri  
- Dhanush
- Kanaparthi Anoohya
- Kashish Kumari
- Lavanya Gorle
- Piyush Upadhyay
- Shaloni Mishra
- Varunraj

## Project Structure
```bash
AI-Speech-Translation/
│
├── data/                      # Collected audio samples
│   ├── english/               # English audio files (.wav)
│   ├── hindi/                 # Hindi audio files (.wav)
│   └── hinglish/              # Mixed language audio files (optional)
│
├── notebooks/                 # Jupyter notebooks for testing and experimentation
│   ├── 01_speech_recognition_test.ipynb    # Test Azure STT on sample files
│   └── 02_auto_lang_detection.ipynb       # Detect language automatically and test recognition
│
├── src/                       # Python scripts for speech recognition and processing
│   ├── recognize_once.py       # Single file or mic recognition
│   ├── continuous_recognition.py # Continuous mic recognition
│   └── auto_detect.py          # Auto language detection + recognition
│
├── results/                   # Outputs and analysis
│   ├── transcriptions/        # Individual transcription text files for each audio
│   │   ├── english_sample1.txt
│   │   └── hindi_sample1.txt
│   └── accuracy_report.xlsx   # Excel file comparing expected vs recognized texts
│
├── docs/                      # Documentation
│   ├── milestone1_report.md   # Milestone 1 report
│   └── setup_instructions.md  # Instructions for setting up environment and running code
│
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Python dependencies for the project
└── README.md                  # Project overview, setup instructions, and team info
```


## How to Run the Code (Setup Steps)

 ### 1. Clone Repository
- git clone <your-repo-link>
cd AI-Speech-Translation

 ### 2. Install Dependencies
pip install -r requirements.txt

### 3. Configure Azure Credentials

Create a .env file in the root directory:

AZURE_SPEECH_KEY= YOUR_SPEECH_KEY

AZURE_REGION=centralindia

### 4. Run Scripts

For Single File Recognition:

python src/recognize_once.py

For Continuous Microphone Recognition:

python src/continuous_recognition.py

### 5. Check Results

Transcriptions are saved in /results/transcriptions/.

Accuracy reports are saved as /results/accuracy_report.xlsx.

### 6. Milestone Documents

- [Milestone 1 Report](docs/milestone1_report.md)
- [Setup Instructions](docs/setup_instructions.md)
