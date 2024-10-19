import assemblyai as aai
from elevenlabs import stream, voice_generation
from openai import OpenAI


class AI_Assistant:
    def __init__(self):
        aai.settings.api_key = "API-KEY"
        self.openapi_client = OpenAI(api_key="API-KEY")
        self.elevenlabs_api_key = "API-KEY"

        self.transcriber = None

        # Prompt
        self.full_transcript = [
            {
                "role": "system",
                "content": "You are a receptionist at a dental clinic. Be resourceful and efficient."
            }
        ]

    ## Step-2: Real time `Speech to Text` transcription with assemblyai

    def start_transcription(self):
        self.transcriber = aai.RealtimeTranscriber(
            sample_rate=16000,
            on_data=self.on_data,
            on_error=self.on_error,
            on_open=self.on_open,
            on_close=self.on_close,
            end_utterance_silence_threshold=1000
        )

        self.transcriber.connect()
        microphone_stream = aai.extras.MicrophoneStream(sample_rate=16000)
        self.transcriber.stream(microphone_stream)

    # def stop_transcription