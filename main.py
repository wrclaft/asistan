import webbrowser
from gtts import gTTS
import speech_recognition as sr
import time
import wikipedia
from time import ctime
import playsound
import os
import random

R = sr.Recognizer()

wikipedia.set_lang("TR")

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            ai_speak(ask)
        audio = R.listen(source)
        try:
            voice_data = R.recognize_google(audio,language=("Tr-tr"))
            print("algılanan ses komutu:", voice_data)
        except sr.UnknownValueError:
            print("böyle bir komut bulunamadı")
        except sr.RequestError:
            print("sistem hatası")
        return voice_data

def ai_speak(audio_string):
    tts = gTTS(text=audio_string,lang="tr")
    r = random.randint(1,100000)
    audio_file = "audio-" + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if "Merhaba" in voice_data:
        ai_speak("Sanada merhaba")
    if "Selamünaleyküm" in voice_data:
        ai_speak('Aleyküm selam')
    if "internette ara" in voice_data:
        kelime = record_audio("Ne aramak istersin")
        kelime=kelime
        url = "https://www.google.com.tr/search?q=" + kelime
        webbrowser.get().open(url)
    if "kimdir" in voice_data:
        kelime=voice_data.split("kimdir", maxsplit=1)
        oge = kelime[0]
        url = "https://www.google.com.tr/search?q=" + oge
        webbrowser.get().open(url)
    if "nerede" in voice_data:
        kelime = voice_data.split("nerede", maxsplit=1)
        oge = kelime[0]
        url = "https://www.google.com.tr/maps/place/" + oge
        ai_speak(oge, "ile alakalı şunları buldum")
        webbrowser.get().open(url)
    if "saat kaç" in voice_data:
        ai_speak("saat:", ctime)

time.sleep(1)

ai_speak('Sebastian Sizi Dinliyor')
while True:
    voice_data = record_audio()
    respond(voice_data)