kisi_sayisi=int(input("Kişi sayısını giriniz: "))

maks= 50

if kisi_sayisi < maks:
    print("sığabilir")
elif kisi_sayisi == maks:
    print("eşit")
else:
    print("sığamaz")
