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
    new_frame=cv2.copyMakeBorder(frame,10,10,10,10,cv2.BORDER_CONSTANT)
    cv2.imshow("Canlı", new_frame)
    cv2.cvtColor
    tus = cv2.waitKey(1)
    if tus ==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()