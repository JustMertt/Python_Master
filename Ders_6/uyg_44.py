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
        yuz=kare[y:y+h,x:x+w]
        kare[y:y+h,x:x+w]=cv2.GaussianBlur(yuz,(99,99),30)

    cv2.imshow("Kamera",kare)
    tus=cv2.waitKey(1)
    if tus==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()