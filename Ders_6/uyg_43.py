import os
import time
import cv2

os.chdir(os.path.dirname(os.path.abspath(__file__)))
yuz_bulucu=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
gulumseme_bulucu=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_smile.xml")
son_cekim=0
kamera=cv2.VideoCapture(0)

while True:
    basarili,kare=kamera.read()
    if not basarili:
        break
    kare=cv2.flip(kare,1)
    gri=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    for (x,y,w,h) in yuz_bulucu.detectMultiScale(gri,1.3,5):
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),3)
        yuz=gri[y:y+h,x:x+w]
        alt_yari=gri[y+h//2:y+h,x:x+w]
        gulumsemeler=gulumseme_bulucu.detectMultiScale(alt_yari,1.7,20)
        if len(gulumsemeler)>0:
            cv2.putText(kare,"Gulumseme Algilandi",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
            if time.time()-son_cekim>3:
                son_cekim=time.time()
                cv2.imwrite("gulumseme.png",kare)
                print("Gulumseme algilandi ve kaydedildi.")
    cv2.imshow("Kamera",kare)
    tus=cv2.waitKey(1)
    if tus==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()