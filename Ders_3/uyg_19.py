import cv2

yol="Ders_3\Resimler\Adsiz-tasarim-2024-06-15T101601.722 copy.jpg"
resim=cv2.imread(yol)
soru= input("Ne eklemek istersiniz(daire/kare): ")
def kare():
    kare_p1_x=int(input("Lütfen p1x kenarını giriniz"))
    kare_p1_y=int(input("Lütfen p1y kenarını giriniz"))
    kare_p2_x=int(input("Lütfen p2x kenarını giriniz"))
    kare_p2_y=int(input("Lütfen p2y kenarını giriniz"))

    cv2.rectangle(resim,(kare_p1_x,kare_p1_y),(kare_p2_x,kare_p2_y),(0,0,255))
def daire():
    daire_merkez_x=int(input("Dairenin merkezinin x eksenini giriniz: "))
    daire_merkez_y=int(input("Dairenin merkezinin y eksenini giriniz: "))
    daire_yaricap=int(input("Dairenin yarıçapını giriniz: "))
    daire_kalinlik=int(input("Dairenin çizgi kalınlığını giriniz(içi dolu olması için -1): "))

    cv2.circle(resim,(daire_merkez_x,daire_merkez_y),daire_yaricap,(255,0,0),daire_kalinlik)


if soru == "kare":
    kare()
    cv2.imshow("at", resim)
elif soru == "daire":
    daire()
    cv2.imshow("at", resim)





cv2.waitKey(0)
cv2.destroyAllWindows()