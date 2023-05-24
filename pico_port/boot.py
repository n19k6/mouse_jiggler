
#f:~/Projects$ /home/abc/.local/bin/picopins --all --licht
#╭───────────────────────────────────────── Raspberry Pi Pico Pinout ─────────────────────────────────────────╮
#│                                                 ┏────┓                                                    │
#│                                            ┏────┫     ┣─────┓                                               │
#│ PWM0 A UART0 TX  I2C0 SDA SPI0 RX      GP0 ┃◎   ┗─────┛    ◎┃ VBUS                                          │
#│ PWM0 B UART0 RX  I2C0 SCL SPI0 CSn     GP1 ┃◎ ▩           ◎┃ VSYS                                          │
#│                                     Ground ┃▣ └─GP25      ▣┃ Ground                                        │
#│ PWM1 A UART0 CTS I2C1 SDA SPI0 SCK     GP2 ┃◎  ▒▒▒        ◎┃ 3v3 En                                        │
#│ PWM1 B UART0 RTS I2C1 SCL SPI0 TX      GP3 ┃◎  ▒▒▒        ◎┃ 3v3 Out                                       │
#│ PWM2 A UART1 TX  I2C0 SDA SPI0 RX      GP4 ┃◎             ◎┃ ADC VRef                                      │
#│ PWM2 B UART1 RX  I2C0 SCL SPI0 CSn     GP5 ┃◎             ◎┃ GP28 / A2  SPI1 RX  I2C0 SDA UART0 TX  PWM6 A │
#│                                     Ground ┃▣             ▣┃ ADC Ground                                    │
#│ PWM3 A UART1 CTS I2C1 SDA SPI0 SCK     GP6 ┃◎   ▓▓▓▓▓▓▓   ◎┃ GP27 / A1  SPI1 TX  I2C1 SCL UART1 RTS PWM5 B │
#│ PWM3 B UART1 RTS I2C1 SCL SPI0 TX      GP7 ┃◎   ▓▓▓▓▓▓▓   ◎┃ GP26 / A0  SPI1 SCK I2C1 SDA UART1 CTS PWM5 A │
#│ PWM4 A UART1 TX  I2C0 SDA SPI1 RX      GP8 ┃◎   ▓▓▓▓▓▓▓   ◎┃ run                                           │
#│ PWM4 B UART1 RX  I2C0 SCL SPI1 CSn     GP9 ┃◎   ▓▓▓▓▓▓▓   ◎┃ GP22       SPI0 SCK I2C1 SDA UART1 CTS PWM3 A │
#│                                     Ground ┃▣             ▣┃ Ground                                        │
#│ PWM5 A UART1 CTS I2C1 SDA SPI1 SCK    GP10 ┃◎             ◎┃ GP21       SPI0 CSn I2C0 SCL UART1 RX  PWM2 B │
#│ PWM5 B UART1 RTS I2C1 SCL SPI1 TX     GP11 ┃◎             ◎┃ GP20       SPI0 RX  I2C0 SDA UART1 TX  PWM2 A │
#│ PWM6 A UART0 TX  I2C0 SDA SPI1 RX     GP12 ┃◎             ◎┃ GP19       SPI0 TX  I2C1 SCL UART0 RTS PWM1 B │
#│ PWM6 B UART0 RX  I2C0 SCL SPI1 CSn    GP13 ┃◎             ◎┃ GP18       SPI0 SCK I2C1 SDA UART0 CTS PWM1 A │
#│                                     Ground ┃▣             ▣┃ Ground                                        │
#│ PWM7 A UART0 CTS I2C1 SDA SPI1 SCK    GP14 ┃◎             ◎┃ GP17       SPI0 CSn I2C0 SCL UART0 RX  PWM0 B │
#│ PWM7 B UART0 RTS I2C1 SCL SPI1 TX     GP15 ┃◎    ◎ ▣ ◎    ◎┃ GP16       SPI0 RX  I2C0 SDA UART0 TX  PWM0 A │
#│                                            ┗───────────────┛                                               │
#│ @gadgetoid                                                                                                 │
#│ https://pico.pinout.xyz                                                                                    │
#╰────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
#f:~/Projects$


import storage, usb_cdc
import board, digitalio
import usb_hid

out = digitalio.DigitalInOut(board.GP14)
out.direction = digitalio.Direction.OUTPUT
out.value = True

print("executing boot.py")

# In this example, the button is wired to connect D2 to +V when pushed.
button = digitalio.DigitalInOut(board.GP15)
button.pull = digitalio.Pull.DOWN

# Disable devices only if button is not pressed.
if not button.value:
    print("test")
    #storage.disable_usb_drive()
    #usb_cdc.disable()

usb_hid.enable((usb_hid.Device.MOUSE,))
