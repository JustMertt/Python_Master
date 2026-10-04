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


    cerceve_rengi=[0,255,0]
    cerceve=cv2.copyMakeBorder(frame,10,10,10,10,cv2.BORDER_CONSTANT,value=cerceve_rengi)
    ayna_frame=cv2.flip(cerceve,0)
    
    cv2.imshow("Kalabalık", ayna_frame)
    tus = cv2.waitKey(25)
    if tus == ord('q'):
        break
video.release()
cv2.destroyAllWindows()