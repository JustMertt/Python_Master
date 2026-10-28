import os
import tempfile

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

tanima=sr.Recognizer()

def konus(metin):
    print("Bilgisyar", metin)
    with tempfile.NamedTemporaryFile(delete=False,suffix=".mp3") as dosya:
        yol = dosya.name
        try:
            gTTS(text=metin,lang="tr").save(yol)
            playsound(yol)
        except Exception as hata:
            print("Ses çalınamadı. Hata: ",hata)
        finally:
            os.remove(yol)

def dinle():
    with sr.Microphone() as mikrofon:
        tanima.adjust_for_ambient_noise(mikrofon,duration=3)
        print("Dinleniyor...")
        try:
            ses=tanima.listen(mikrofon,timeout=3,phrase_time_limit=4)
        except sr.WaitTimeoutError:
            return " "
        try:
            metin= tanima.recognize_google(ses,language="tr-TR")
        except (sr.UnknownValueError,sr.RequestError):
            return " "
        metin=metin.replace("I","ı").replace("İ","i").lower()
        print("Sen: ",metin)
        return metin