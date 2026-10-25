from gtts import gTTS
import os

metin = input("Ne söylemesini istersiniz: ")
dil = input("Dil(tr için boş bırakınız): ")

if dil == "":
    dil = "tr"

tts = gTTS(text=metin, lang=dil)

tts.save("hello.mp3")

os.system("hello.mp3")