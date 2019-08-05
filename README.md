# mouse_jiggler
This repository contains information about turning a nRF52840 Dongle (PCA10059) into a mouse jiggler device.

A mouse jiggler is a hardware device that simulates tiny mouse movements which prevent the operation system to enter standby mode due to missing keyboard or mouse interactions.

You have differen options to get a mouse jiggler device:
- buy a commercial mouse jiggler device for less than 20 EUR
- buy a circuit python board from adafruit and copy a python control script to it
- buy a nRF52840 Dongle device, flash the boot loader, install circuit python and copy a python control script to it

Fortunately everything has already been done and documented at different web sites before.
This repository only contains a summary of existing information found.

Step 1:
Install UF2 Bootloader onto nRF52840 Dongle by following the detailed instructions given at [2].
You need an raspberry pi and you have to solder two pin headers temporarily.
The mentioned hex-file in available at [3].

Step 2:
Install CircuitPython

Step 3:
Add main.py script

I added an additional video on vimeo to document the function of the device.

Contents:

File | Description
------------ | -------------
README.md | This file
webmirror_circuitpython_nrf52840_dongle_openocd_pi_tutorial.pdf | mirror of robotron website on 2019-07-31
nRF52840_Dongle_product_brief.pdf | brief description from nordic about nRF52840-Dongle

Links:
- [1] (www.circuitpython.org)
- [2] (https://www.rototron.info/circuitpython-nrf52840-dongle-openocd-pi-tutorial/)
- [3] (https://github.com/adafruit/Adafruit_nRF52_Bootloader)
- [4] (https://vimeo.com/333207415)
- [5] (https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-Dongle/GetStarted)

