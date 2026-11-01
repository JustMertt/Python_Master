from ses import *
import webbrowser

siteler = {
    "youtube": "https://www.youtube.com/",
}

konus("hangi siteyi açayım")
while True:
    ses= dinle()
    if ses =="":
        continue
    if "görüşürüz" in ses:
        konus("görüşürüz")
        break
    cevap="Webde bu sonuçları buldum"

    bulundu= False
    for site in siteler:
        if site in ses:
            konus(f"{site} açılıyor")
            webbrowser.open(siteler[site])
            bulundu= True
            break
    if not bulundu:
        konus("hata")