secim=input("ne almak istiyorsunuz(hamburger, pizza): ")
toplam=0
if secim == "hamburger":
    hamburger=input("hamburger seçiniz(S,M,L): ")
    icecek= input("içcecek seçiniz(cola,fanta,fusetea,ayran,su) istemiyorsanız boş bırakınız: ")
    if hamburger == "S":
        toplam+=150
    elif hamburger == "M":
        toplam += 200
    elif hamburger == "M":
        toplam += 250
    else:
        print("Yanlış veya boş boy girdiniz")


    if icecek == "cola":
        toplam += 70
    elif icecek == "fanta":
        toplam += 80
    elif icecek == "fusetea":
        toplam += 90
    elif icecek == "ayran":
        toplam += 50
    elif icecek == "su":
        toplam += 20



elif secim == "pizza":
    boy=input("İstediğiniz pizzanın boyunu giriniz(S,M,L,XL): ")
    peynir=input("peynir istiyormusunuz?(E,H): ")
    hamur=input("hamur tipini giriniz(ince,kalın) ve normal seçmek için boş bırakınız")
    icecek= input("içcecek seçiniz(cola,fanta,fusetea,ayran,su) istemiyorsanız boş bırakınız: ")



    if boy == "S":
        toplam += 250
        if peynir == "E":
            toplam +=20

    elif boy == "M":
        toplam += 300
        if peynir == "E":
            toplam +=30

    elif boy == "L":
        toplam += 350
        if peynir == "E":
            toplam +=30

    elif boy == "XL":
        toplam += 400
        if peynir == "E":
            toplam +=30

    else:
        print("Yanlış boy girdiniz")

    if hamur == "ince":
        toplam += 10
    if hamur == "kalın":
        toplam += 20



    if icecek == "cola":
        toplam += 70
    elif icecek == "fanta":
        toplam += 80
    elif icecek == "fusetea":
        toplam += 90
    elif icecek == "ayran":
        toplam += 50
    elif icecek == "su":
        toplam += 20

print(toplam)