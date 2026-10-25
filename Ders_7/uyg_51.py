#Text-To-Speech

from gtts import gTTS
import os


tts = gTTS(text="Merhaba nasılsın", lang='tr')

tts.save("hello.mp3")

os.system("hello.mp3")