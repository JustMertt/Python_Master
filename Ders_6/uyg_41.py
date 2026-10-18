import cv2
yuz_bulucu=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
göz_bulucu=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_eye.xml")
kamera=cv2.VideoCapture(0)

while True:
    basarili,kare=kamera.read()
    if not basarili:
        break
    kare=cv2.flip(kare,1)
    gri=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    yuzler=yuz_bulucu.detectMultiScale(gri,1.3,5)

    for (x,y,w,h) in yuzler:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),3)
        yuz=gri[y:y+h,x:x+w]
        gozler=göz_bulucu.detectMultiScale(yuz,1.1,10)



        for(gx,gy,gw,gh) in gozler:
            cv2.rectangle(kare,(x+gx,y+gy),(x+gx+gw,y+gy+gh),(0,255,0),2)
    cv2.imshow("Kamera",kare)
    tus=cv2.waitKey(1)
    if tus==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()