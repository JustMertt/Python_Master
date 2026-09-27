import cv2

yol="Ders_3/Resimler/Adsiz-tasarim-2024-06-15T101601.722.jpg"
resim=cv2.imread(yol)

yeni_genişlik=1000
yeni_yükseklik=400
cv2.imshow("At",resim)
değişmiş_res=cv2.resize(resim,(yeni_genişlik,yeni_yükseklik))

cv2.imshow("At",değişmiş_res)








cv2.waitKey(0)
cv2.destroyAllWindows()