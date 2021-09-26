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