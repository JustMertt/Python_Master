import cv2

yol="Ders_3/Resimler/Adsiz-tasarim-2024-06-15T101601.722.jpg"
resim=cv2.imread(yol)
yeni_resim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)


cv2.imshow("At",yeni_resim)
cv2.imwrite("Ders_3/Resimler/Adsiz-tasarim-2024-06-15T101601.722.jpg",yeni_resim)






cv2.waitKey(0)
cv2.destroyAllWindows()