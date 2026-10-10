import cv2

videosoru=input("Hangi Video(New York/Kalabalık): ")
if videosoru == "New York" or videosoru == "new york":
    yol = "Ders_4/Videolar/times_square.mp4"
elif videosoru=="Kalabalık" or videosoru=="kalabalık" :
    yol = "Ders_4/Videolar/KALABALIK İNSANLAR (HD) - STOK VİDEO.mp4"
else:
    print("Video ismini yanlış yazdınız(Kalabalık/New York)")
    exit()

video = cv2.VideoCapture(yol)


sekil=input("Ne çizmek istersiniz(daire/kare/yazı): ")
if sekil == "kare":
    kare_p1_x=int(input("Lütfen p1x kenarını giriniz: "))
    kare_p1_y=int(input("Lütfen p1y kenarını giriniz: "))
    kare_p2_x=int(input("Lütfen p2x kenarını giriniz: "))
    kare_p2_y=int(input("Lütfen p2y kenarını giriniz: "))
    kare_kalinlik=int(input("Lütfen karenin kalınlığını giriniz: "))
    r = int(input("Lütfen karenin R değerini giriniz: "))
    g = int(input("Lütfen karenin G değerini giriniz: "))
    b = int(input("Lütfen karenin B değerini giriniz: "))
elif sekil == "daire":
    daire_merkez_x=int(input("Dairenin merkezinin x eksenini giriniz: "))
    daire_merkez_y=int(input("Dairenin merkezinin y eksenini giriniz: "))
    daire_yaricap=int(input("Dairenin yarıçapını giriniz: "))
    daire_kalinlik=int(input("Dairenin çizgi kalınlığını giriniz(içi dolu olması için -1): "))
    r = int(input("Lütfen dairenin R değerini giriniz: "))
    g = int(input("Lütfen dairenin G değerini giriniz: "))
    b = int(input("Lütfen dairenin B değerini giriniz: "))
elif sekil == "yazı":
    metin=input("Görmek istediğiniz yazıyı giriniz: ")
    r = int(input("Lütfen yazının R değerini giriniz: "))
    g = int(input("Lütfen yazının G değerini giriniz: "))
    b = int(input("Lütfen yazının B değerini giriniz: "))
else:
    print("Şekili yanlış girdiniz")
    exit()




if video.isOpened() == False:
    print("Video açılamadı")
    exit()

while True:
    ret, frame = video.read()
    if ret == False:
        print("kare alınamadı")
        break
    if sekil== "kare":
        cv2.rectangle(frame,(kare_p1_x,kare_p1_y),(kare_p2_x,kare_p2_y),(b,g,r),kare_kalinlik)
    elif sekil=="daire":
        cv2.circle(frame,(daire_merkez_x,daire_merkez_y),daire_yaricap,(b,g,r),daire_kalinlik)
    elif sekil=="yazı":
        cv2.putText(frame,metin,(400,50),cv2.FONT_ITALIC,1,(b,g,r),2,cv2.LINE_8)
    
    cv2.imshow("Kalabalık", frame)
    tus = cv2.waitKey(25)
    if tus == ord('q'):
        break
video.release()
cv2.destroyAllWindows()