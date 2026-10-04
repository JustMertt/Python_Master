import cv2

yol = "Ders_4/Videolar/times_square.mp4"
video = cv2.VideoCapture(yol)
if video.isOpened() == False:
    print("Video açılamadı")
    exit()

genişlik=1200
yükseklik = 100
print(f"Genişlik: {genişlik}")
print(f"Yükseklik: {yükseklik}")
while True:
    ret, frame = video.read()
    if ret == False:
        print("kare alınamadı")
        break

    yeni_boyut=cv2.resize(frame,(genişlik,yükseklik))
    cv2.imshow("Kalabalık", yeni_boyut)
    tus = cv2.waitKey(25)
    if tus == ord('q'):
        break
video.release()
cv2.destroyAllWindows()