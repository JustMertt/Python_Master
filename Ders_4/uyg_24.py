import cv2

yol = "Ders_4/Videolar/times_square.mp4"
video = cv2.VideoCapture(yol)
if video.isOpened() == False:
    print("Video açılamadı")
    exit()

genişlik=video.get(cv2.CAP_PROP_FRAME_WIDTH)
yükseklik = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"Genişlik: {genişlik}")
print(f"Yükseklik: {yükseklik}")
while True:
    ret, frame = video.read()
    if ret == False:
        print("kare alınamadı")
        break
    cv2.imshow("Kalabalık", frame)
    tus = cv2.waitKey(25)
    if tus == ord('q'):
        break
video.release()
cv2.destroyAllWindows()