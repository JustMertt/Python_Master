import sys
from PyQt5.QtWidgets import *
from video_ui import Ui_MainWindow
import cv2


class gui_pencere(QMainWindow):
    def __init__(self):
        super(gui_pencere, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.kare_done.clicked.connect(self.kare_done)
        self.ui.daire_done.clicked.connect(self.daire_done)
        self.ui.yazi_done.clicked.connect(self.yazi_done)
    def kare_done(self):
        self.kare_p1x=self.ui.kare_p1x.text()
        self.kare_p1y=self.ui.kare_p1y.text()
        self.kare_p2x=self.ui.kare_p2x.text()
        self.kare_p2y=self.ui.kare_p2y.text()
        
    def daire_done(self):
        self.daire_px=self.ui.daire_px.text()
        self.daire_py=self.ui.daire_py.text()
        self.daire_yaricap=self.ui.daire_yaricap.text()
    def yazi_done(self):
        self.yazi=self.ui.kare_p1x_3.text()





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
        cv2.circle(frame,(daire_px,daire_py),daire_yaricap,(0,0,255),-1)
    elif sekil=="yazı":
        cv2.putText(frame,yazi,(400,50),cv2.FONT_ITALIC,1,(b,g,r),2,cv2.LINE_8)
    
    cv2.imshow("Kalabalık", frame)
    tus = cv2.waitKey(25)
    if tus == ord('q'):
        break



uygulama = QApplication(sys.argv)
pencere = gui_pencere()
pencere.show()
sys.exit(uygulama.exec_())