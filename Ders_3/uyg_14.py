import cv2

yol="Ders_3/Resimler/Adsiz-tasarim-2024-06-15T101601.722.jpg"
resim=cv2.imread(yol)
ayna_frame= cv2.flip(resim,1)
cv2.imshow("At",ayna_frame)


cv2.waitKey(0)
cv2.destroyAllWindows()