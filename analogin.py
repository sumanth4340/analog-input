
import Adafruit_BBIO.ADC as ADC
ADC.setup()
from time import sleep
analogpin="P9_33"
while(1):
        potvalue=ADC.read(analogpin)
        print "potmeter vale =",potvalue
        sleep(0.5)
