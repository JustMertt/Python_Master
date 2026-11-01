from ses import *

konus("Sesli asistan başlatılıyor")

while True:
    soz=dinle()
    if soz =="":
        continue
    if "görüşürüz" in soz:
        konus("görüşürüz")
        break

    if "merhaba" in soz:
        konus("Merhaba ,hoş geldin")
    elif"nasılsın" in soz:
        konus("iyiyim, sen nasılsın?")
    elif "adın ne" in soz:
        konus("ben sesli asistanım")
