import cv2

yol="Ders_3/Resimler/Adsiz-tasarim-2024-06-15T101601.722.jpg"
resim=cv2.imread(yol)
cerceve_rengimiz=[169,204,59]
cerceve=cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value=cerceve_rengimiz)
cv2.imshow("At",cerceve)


cv2.waitKey(0)
cv2.destroyAllWindows()