from ses import *

sorular = {
    "Türkiyenin başkenti neresidir?": "ankara",
    "Python kelimesinin anlamı olan hayvan hangisidir?": "yılan",
    "Güneş sistemindeki en büyük gezegen hangisidir?": "jüpiter",
    "Gökkuşağının en üstündeki renk hangisidir?": "kırmızı",
    "Atatürk hangi şehirde doğmuştur?": " selanik",
    "En iyi futbol takımı?":"galatasaray"
}

puan=0
konus("Bilgi yarışmasına hoşgeldin sana sorulan sorulara cevap ver")

for soru,cevap in sorular.items():
    konus(soru)
    ses=dinle()
    if cevap in ses:
        puan += 10
        konus("doğru bildin")
    else:
        konus(f"yanlış cevap doğrusu {cevap}")
konus(f"Yarışma bitti puanınız {puan}")