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
    cv2.rectangle(frame,(10,20),(30,40),(0,0,255),3,1)
    cv2.imshow("Canlı", frame)
    cv2.cvtColor
    tus = cv2.waitKey(1)
    if tus ==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()