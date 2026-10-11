import cv2

kamera = cv2.VideoCapture(0)
if kamera.isOpened==False:
    print("Kamer açıldı")
    exit()

while True:
    ret, frame=kamera.read()
    if ret == False:
        print("Kare alınamadı")
        break
    new_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Canlı", new_frame)
    tus = cv2.waitKey(1)
    if tus ==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()