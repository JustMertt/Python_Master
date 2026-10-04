import cv2

yol = "Ders_4/Videolar/times_square.mp4"
video = cv2.VideoCapture(yol)
if video.isOpened() == False:
    print("Video açılamadı")
    exit()

while True:
    ret, frame = video.read()
    if ret == False:
        print("kare alınamadı")
        break
    cv2.rectangle(frame,(200,40),(400,250),(0,255,0),4)
    cv2.rectangle(frame,(300,150),(700,250),(255,0,0),5)
    cv2.imshow("Kalabalık", frame)
    tus = cv2.waitKey(25)
    if tus == ord('q'):
        break
video.release()
cv2.destroyAllWindows()