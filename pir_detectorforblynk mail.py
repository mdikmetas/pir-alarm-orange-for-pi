from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

import time
import datetime
import os
import sys
import blynklib

blynk = blynklib.Blynk('scj8uYdDbHItjzwxDiQOYkeBvX99HoZHO')

gpio.init()
hareket = port.PA20

gpio.setcfg(hareket, gpio.INPUT)

while True:
    blynk.run()
    if gpio.input(hareket):
        print "hareketvar" " " + str(datetime.datetime.now())
        time.sleep(1)
#        blynk.run()
        blynk.email("muratdikmetas@gmail.com", "CAFE ALARM", "CAFEDE HAREKET VAR");









