import cv2



yol="Ders_3\Resimler\Adsiz-tasarim-2024-06-15T101601.722 copy.jpg"
resim=cv2.imread(yol)

cv2.rectangle(resim,(600,10),(770,180),(0,0,255),5)


cv2.circle(resim,(410,560),40,(255,0,0),5)
cv2.circle(resim,(670,560),40,(255,0,0),5)
cv2.circle(resim,(320,568),40,(255,0,0),5)
cv2.circle(resim,(130,568),40,(255,0,0),5)



cv2.putText(resim,"AT",(400,70),cv2.FONT_ITALIC,1,(0,0,255),2,cv2.LINE_8)
cv2.imshow("kareli at", resim)




#cv2.line(resim,(200,250),(540,550),(0,255,0),2)

cv2.waitKey(0)
cv2.destroyAllWindows()