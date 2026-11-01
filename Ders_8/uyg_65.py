from ses import *

cevaplar= {
    "merhaba":"Merhaba , hoş geldin",
    "nasılsın": "İyiyim, sen nasılsın?",
    "teşekkür": "rica ederim!",
}


konus("merhaba sesli asistan şu anda başlıyor")

while True:
    ses= dinle()
    if ses =="":
        continue
    if "görüşürüz" in ses:
        konus("Görüşürüz")
        break
    cevap="Webde bu sonuçları buldum"
    for anahtar in cevaplar:
        if anahtar in ses:
            cevap = cevaplar[anahtar]
    konus(cevap)