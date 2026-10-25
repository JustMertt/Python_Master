import pyttsx3

engine = pyttsx3.init()

metin="galatasaray şampiyon"

engine.say(metin)

engine.setProperty("rate",100)
engine.setProperty("volume", 0.9)
engine.setProperty("lang", 'tr')
engine.save_to_file(metin, 'audio.mp3')
engine.runAndWait()