tercih=input("Sinemamı Tiyatromu: ")
ogrenci = input("Öğrencimisiniz(E/H): ")
fiyat=0
if tercih == "sinema":
    fiyat += 150
    if ogrenci == "E":
        fiyat = fiyat / 2
else:
    fiyat += 100
    if ogrenci == "E":
        fiyat= fiyat/2

print(fiyat)