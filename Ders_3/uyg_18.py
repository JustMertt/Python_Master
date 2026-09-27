import cv2

yol="Ders_3\Resimler\Adsiz-tasarim-2024-06-15T101601.722 copy.jpg"
resim=cv2.imread(yol)

cv2.rectangle(resim,(200,40),(400,250),(0,0,255),5)
cv2.line(resim,(200,250),(540,550),(0,255,0),2)
cv2.circle(resim,(500,560),40,(255,0,0),5)
cv2.putText(resim,"AT",(400,400),cv2.FONT_ITALIC,1,(255,255,0),2,cv2.LINE_8)
cv2.imshow("kareli at", resim)






cv2.waitKey(0)
cv2.destroyAllWindows()