
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython
# https://learn.adafruit.com/building-circuitpython/customizing-usb-devices

import time
import usb_hid
import Mouse

time.sleep(3)

m = Mouse(usb_hid.devices)
m.move(100,0,0)
time.sleep(0.5)
m.move(-100,0,0)

while True:
    time.sleep(60)
    m.move(1,1,0)
    time.sleep(0.2)
    m.move(-1,-1,0)
    time.sleep(0.2)



