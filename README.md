# ai-receiptionist-bot

This is an ai receptionist chatbot for creating and maintaining any doctor's appointment. The entire development flow
involves these
steps:

## Step-1: Install python libraries

    - assemblyai
    - openai
    - elevenlabs
    - mpv
    - portaudio
Common dependencies:
```
brew install portaudio
pip install "assemblyai[extras]"
pip install elevenlabs==0.3.0b0
brew install mpv
pip install --upgrade openai
```

If you want to install them in mac using virtual environment [Python3/pip3] then follow these commands:
```
mkdir python-virtual-environments
cd python-virtual-environments/
python3 -m venv ai-venv
cd ..
python-virtual-environments/ai-venv/bin/pip3 install "assemblyai[extras]"
brew install rust
python-virtual-environments/ai-venv/bin/pip3 install elevenlabs
brew install mpv
python-virtual-environments/ai-venv/bin/pip3 install --upgrade openai
```

## Step-2: Real time `Speech to Text` transcription with assemblyai
## Step-3: Pass real time transcript to OpenAI
## Step-4: Live streaming the response as audio to the user using ElevenLabs
