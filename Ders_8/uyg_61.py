from ses import *
import time

konus("tekrar etme modu")

while True:
    ses = dinle()


    if ses == "":
        continue
    if "görüşürüz" in ses:
        break
    konus(ses)