import cv2

yol="Ders_3\Resimler\Adsiz-tasarim-2024-06-15T101601.722 copy.jpg"
resim=cv2.imread(yol)

def kare():
    kare_p1_x=int(input("Lütfen p1x kenarını giriniz"))
    kare_p1_y=int(input("Lütfen p1y kenarını giriniz"))
    kare_p2_x=int(input("Lütfen p2x kenarını giriniz"))
    kare_p2_y=int(input("Lütfen p2y kenarını giriniz"))

    cv2.rectangle(resim,(kare_p1_x,kare_p1_y),(kare_p2_x,kare_p2_y),(0,0,255))









cv2.waitKey(0)
cv2.destroyAllWindows()