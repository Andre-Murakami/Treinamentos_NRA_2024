import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import os

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo:")
        audio = recognizer.listen(source)

    try:
        print("Reconhecendo...")
        text = recognizer.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {text}")
        return text
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse.")
        return None
    except sr.RequestError:
        print("Erro ao solicitar resultados do serviço de reconhecimento de fala.")
        return None

def text_to_speech(text):
    tts = gTTS(text=text, lang='pt-br')
    audio_file = "output.mp3"
    tts.save(audio_file)

    # Reproduzir o áudio usando pydub
    audio = AudioSegment.from_mp3(audio_file)
    play(audio)
    
    # Remover o arquivo de áudio após a reprodução
    os.remove(audio_file)

if __name__ == "__main__":
    texto = recognize_speech()
    if texto:
        text_to_speech(texto)
