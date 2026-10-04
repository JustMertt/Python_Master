import cv2


# 1. ADIM: Video Seçimi
videosoru=input("Hangi Video(New York/Kalabalık): ")
if videosoru == "New York":
    yol = "Ders_4/Videolar/times_square.mp4"
elif videosoru=="Kalabalık":
    yol = "Ders_4/Videolar/KALABALIK İNSANLAR (HD) - STOK VİDEO.mp4"
# İPUCU: Kullanıcı geçersiz bir isim yazarsa 'yol' değişkeni tanımsız kalabilir.
# Buraya bir 'else' ekleyip varsayılan bir yol atayabilir veya programı sonlandırabilirsin.

video = cv2.VideoCapture(yol)

# 2. ADIM: Çizim Fonksiyonları
# DİKKAT: Fonksiyonların içinde input() bırakılırsa, video oynarken her karede video donar ve girdi bekler.
# MANTIK: Fonksiyonların görevi sadece çizim yapmak olmalı. 
# Kullanıcıdan soru sormak yerine, dışarıdan parametre olarak o anki kareyi (frame) 
# ve önceden alınmış koordinatları/verileri almalıdır.
def kare():
    kare_p1_x=int(input("Lütfen p1x kenarını giriniz"))
    kare_p1_y=int(input("Lütfen p1y kenarını giriniz"))
    kare_p2_x=int(input("Lütfen p2x kenarını giriniz"))
    kare_p2_y=int(input("Lütfen p2y kenarını giriniz"))

    cv2.rectangle(frame,(kare_p1_x,kare_p1_y),(kare_p2_x,kare_p2_y),(0,0,255))

def daire():
    daire_merkez_x=int(input("Dairenin merkezinin x eksenini giriniz: "))
    daire_merkez_y=int(input("Dairenin merkezinin y eksenini giriniz: "))
    daire_yaricap=int(input("Dairenin yarıçapını giriniz: "))
    daire_kalinlik=int(input("Dairenin çizgi kalınlığını giriniz(içi dolu olması için -1): "))

    cv2.circle(frame,(daire_merkez_x,daire_merkez_y),daire_yaricap,(255,0,0),daire_kalinlik)

def yazi():
    metin=input("Görmek istediğiniz yazıyı giriniz: ")
    cv2.putText(frame,metin,(400,50),cv2.FONT_ITALIC,1,(0,0,255),2,cv2.LINE_8)


# 3. ADIM: Kullanıcı Tercihlerinin Döngüden Önce Alınması
sekil=input("Ne çizmek istersiniz(daire/kare/yazı): ")

# MANTIK: Kullanıcı hangi şekli seçtiyse, o şekle ait koordinat veya metin sorularını
# BURADA (video döngüsüne girmeden önce, tek seferlik) sormalısın ve değişkenlere kaydetmelisin.
# Örneğin:
# - Eğer daire seçildiyse -> merkez, yarıçap bilgilerini burada sor.
# - Eğer kare seçildiyse -> köşe koordinatlarını burada sor.
# - Eğer yazı seçildiyse -> metin içeriğini burada sor.
# (Aşağıdaki şart bloğunu if / elif / else şeklinde bu mantıkla tamamlayabilirsin)
# if sekil == "daire":
#     ...


if video.isOpened() == False:
    print("Video açılamadı")
    exit()

# 4. ADIM: Video Oynatma ve Çizim Döngüsü
while True:
    ret, frame = video.read()
    if ret == False:
        print("kare alınamadı")
        break
    
    # MANTIK: Yeni kare başarıyla okunduktan sonra, ekrana basılmadan hemen önce:
    # Kullanıcının en başta seçtiği şekle göre (if sekil == ...) ilgili çizim fonksiyonunu
    # çağırıp bu 'frame' üzerine çizimini yapmalısın.

    cv2.imshow("Kalabalık", frame)
    tus = cv2.waitKey(25)
    if tus == ord('q'):
        break
video.release()
cv2.destroyAllWindows()