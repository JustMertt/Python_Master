#Text-To-Speech

from gtts import gTTS
import os
import speech_recognition as sr



tanima = sr.Recognizer()

with sr.Microphone() as mikrofon:
    print("Ortam gürültüsü ölçülüyor...")
    tanima.adjust_for_ambient_noise(mikrofon, duration=1)
    print("Dinleniyor: ")
    ses=tanima.listen(mikrofon)

metin = tanima.recognize_google(ses,language="tr-TR")
print("söylediğin metin: ",metin)

tts = gTTS(text=metin, lang='tr')

tts.save("hello.mp3")

os.system("hello.mp3")
