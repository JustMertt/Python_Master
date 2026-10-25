from gtts import gTTS
import os


ttsmerhaba = gTTS(text="Merhaba", lang='tr')
ttsmerhaba.save("merhaba.mp3")

ttshello = gTTS(text="Hello", lang='en')
ttshello.save("hello.mp3")

ttsbonjour = gTTS(text="Bonjour", lang='fr')
ttsbonjour.save("bonjour.mp3")

ttshallo = gTTS(text="Hallo",lang="de")
ttshello.save("hallo.mp3")


os.system("hello.mp3")