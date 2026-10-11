import cv2
yuz_bulucu = cv2.CascadeClassifier("Ders_5/haarcascade/haarcascade_frontalface_default.xml")
kamera=cv2.VideoCapture(0)

while True:
    basarili,frame=kamera.read()
    if not basarili:
        break
    flipframe=cv2.flip(frame,1)

    gray=cv2.cvtColor(flipframe,cv2.COLOR_BGR2GRAY)
    yuzler=yuz_bulucu.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in yuzler:
        cv2.rectangle(flipframe,(x,y),(x+w,y+h),(0,0,255,2),5)
    cv2.imshow("kamera",flipframe)
    tus=cv2.waitKey(1)
    if tus == ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()