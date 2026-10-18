import cv2


yuz_bulucu=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
kamera=cv2.VideoCapture(0)

while True:
    basarili,kare=kamera.read()
    if not basarili:
        break
    kare=cv2.flip(kare,1)
    gri=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    for (x,y,w,h) in yuz_bulucu.detectMultiScale(gri,1.3,5):
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),3)
        yuz_sayisi=len(yuz_bulucu.detectMultiScale(gri,1.3,5))
        cv2.putText(kare,"Yuz Sayisi: "+str(yuz_sayisi),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow("Kamera",kare)
    tus=cv2.waitKey(1)
    if tus==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()