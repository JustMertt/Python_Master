import os
import datetime

from ses import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

konus("Not defteri hazır konuş ben kaydedeyim")

while True:
    ses= dinle()
    if ses=="":
        continue
    if "görüşürüz" in ses:
        konus("notlar kaydedldi görüşürüz")
        break

    saat = datetime.datetime.now().strftime("%H,%M")
    with open("notlar.txt","+a",encoding="utf-8") as dosya:
        dosya.write(saat+"-"+ses+"\n")
    konus("not alındı")