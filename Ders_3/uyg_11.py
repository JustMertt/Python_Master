import cv2

yol="Ders_3/Resimler/Adsiz-tasarim-2024-06-15T101601.722.jpg"
resim=cv2.imread(yol)
cv2.imshow("At",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()