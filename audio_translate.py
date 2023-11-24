from dotenv import load_dotenv
import os
from pathlib import Path
import openai
import random
import string

id = random.randint(1,9999)
namefile = f"audio_{id}.mp3"

load_dotenv()
key=os.getenv("API_KEY")

# FUNCTIONS
def newFileName(type,extension):
    number=random.randint(1,9999)
    characters = random.choices(string.ascii_uppercase, k=3)
    newName = type + "".join(characters) + str(number) + extension
    return newName


# OPENAI
openai.api_key = key

# SPEECH
def generate_speech(prompt):
    namefile = newFileName("audio",".mp3")
    speech_file_path = Path(__file__).parent / namefile
    response = openai.audio.speech.create(
      model="tts-1",
      voice="onyx",
      input=prompt,
      response_format="mp3",
      speed=0.9 # 0.1 - 3.0
    )
    print("Create successfully: " + namefile)
    return response.stream_to_file(speech_file_path)

generate_speech("Se você deseja gerar duas letras aleatórias em Python, você pode usar o módulo random em combinação com a biblioteca string.")

# Transcription
def generate_transcription(file):
    audio_file = open(file, "rb")
    transcript = openai.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file,
    language="en",
    response_format="json"
    )
    print(transcript.text)
    return transcript

# generate_transcription("audioFRP1170.mp3")

def generate_translation(file):
      audio_file = open("speech.mp3", "rb")
      transcript = openai.audio.translations.create(
      model="whisper-1", 
      file=audio_file,
      response_format="json",
      temperature=0.5
      )
      print(transcript.text)

# generate_translation("audioFRP1170.mp3")