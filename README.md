# mouse_jiggler
This repository contains information about turning an nRF52840 Dongle (PCA10059) into a mouse jiggler device.

A mouse jiggler is a hardware device that simulates tiny mouse movements which prevent the operation system to enter standby mode due to missing keyboard or mouse interactions.

You have different options to get a mouse jiggler device:
- buy a commercial mouse jiggler device for less than 20 EUR
- buy a circuit python board from adafruit and copy a python control script to it
- buy a nRF52840 Dongle device, flash the boot loader, install circuit python and copy a python control script to it

Fortunately everything has already been done and documented at different web sites before.
This repository only contains a summary of existing information found.

Step 1:
Install UF2 bootloader onto nRF52840 Dongle by following the detailed instructions given at [2].
You need a raspberry pi and you have to solder two pin headers temporarily.
The mentioned hex-file in available at [3].

Step 2:
To update circuitpython insert the device into an usb port and check version mentioned in
file boot_out.txt, e.g. 'Adafruit CircuitPython 4.0.1 on 2019-05-22; PCA10059 nRF52840 Dongle with nRF52840'.
Download the appropriate uf2-file from [1] via click on 'Download->nRF52840 Dongle (PCA10059)->DOWNLOAD .UF2 NOW'.
Double click the reset button and wait until usb share NRF52BOOT is available.
Copy the downloaded file 'adafruit-circuitpython-pca10059-en_US-4.1.0.uf2' onto the usb share.
After the file has been copied the device reboots and appears as usb share CIRCUITPY.
Check the content of the file boot_out.txt, which should show the new version of circuitpython.

Step 3:
To install the adafruit_hid library download the latest version of adafruit-circuitpython-bundle-py-<YYYYMMDD>.zip
from [7], e.g. adafruit-circuitpython-bundle-py-20190805.zip and extract it.
Create a directory named lib on the usb share CIRCUITPY and copy the folder adafruit_hid from the extracted zip-file into
the new directory.

Step 4:
Connect to REPL and experiment with the adafruit_hid library. 

Step 5:
Create a file main.py with the following content and copy it to the CIRCUITPY.
```python
import time
import board
from adafruit_hid.mouse import Mouse

time.sleep(10)

m = Mouse()

while True:
    m.move(2,2,0)
    time.sleep(0.2)
    m.move(-2,-2,0)
    time.sleep(0.2)
```

I added an additional video on vimeo to document the function of the device.

Contents:

File | Description
------------ | -------------
README.md | This file
webmirror_circuitpython_nrf52840_dongle_openocd_pi_tutorial.pdf | mirror of robotron website on 2019-07-31
nRF52840_Dongle_product_brief.pdf | brief description from nordic about nRF52840-Dongle

Links:
- [1] (https://circuitpython.org/)
- [2] (https://www.rototron.info/circuitpython-nrf52840-dongle-openocd-pi-tutorial/)
- [3] (https://youtu.be/R5wub5ywzTU)
- [4] (https://github.com/adafruit/Adafruit_nRF52_Bootloader)
- [5] (https://vimeo.com/333207415)
- [6] (https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-Dongle/GetStarted)
- [7] (https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases)

