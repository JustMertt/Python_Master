from ses import *
import webbrowser

konus("Ne arayayım")
while True:
    soz=dinle()
    if soz== "":
        continue
    if "görüşürüz" in soz:
        konus("görüşürüz")
        break
    if soz.endswith(" ara"):
        aranan=soz[:-4]
        konus(f"{aranan} için arama yapılıyor")
        webbrowser.open("https://www.google.com/search?q="+ aranan.replace("", "+"))
    else:
        konus("hata")