
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython
# https://learn.adafruit.com/building-circuitpython/customizing-usb-devices

import time
import usb_hid
import math

time.sleep(1)

def find_device(devices, *, usage_page, usage):
    """Search through the provided list of devices to find the one with the matching usage_page and
    usage."""
    if hasattr(devices, "send_report"):
        devices = [devices]
    for device in devices:
        if (
            device.usage_page == usage_page
            and device.usage == usage
            and hasattr(device, "send_report")
        ):
            return device
    raise ValueError("Could not find matching HID device.")

class Mouse:
    """Send USB HID mouse reports."""

    LEFT_BUTTON = 1
    """Left mouse button."""
    RIGHT_BUTTON = 2
    """Right mouse button."""
    MIDDLE_BUTTON = 4
    """Middle mouse button."""

    def __init__(self, devices):
        """Create a Mouse object that will send USB mouse HID reports.
        Devices can be a list of devices that includes a keyboard device or a keyboard device
        itself. A device is any object that implements ``send_report()``, ``usage_page`` and
        ``usage``.
        """
        self._mouse_device = find_device(devices, usage_page=0x1, usage=0x02)

        # Reuse this bytearray to send mouse reports.
        # report[0] buttons pressed (LEFT, MIDDLE, RIGHT)
        # report[1] x movement
        # report[2] y movement
        # report[3] wheel movement
        self.report = bytearray(4)

        # Do a no-op to test if HID device is ready.
        # If not, wait a bit and try once more.
        try:
            self._send_no_move()
        except OSError:
            time.sleep(1)
            self._send_no_move()

    def press(self, buttons):
        """Press the given mouse buttons.
        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.
        Examples::
            # Press the left button.
            m.press(Mouse.LEFT_BUTTON)
            # Press the left and right buttons simultaneously.
            m.press(Mouse.LEFT_BUTTON | Mouse.RIGHT_BUTTON)
        """
        self.report[0] |= buttons
        self._send_no_move()

    def release(self, buttons):
        """Release the given mouse buttons.
        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.
        """
        self.report[0] &= ~buttons
        self._send_no_move()

    def release_all(self):
        """Release all the mouse buttons."""
        self.report[0] = 0
        self._send_no_move()

    def click(self, buttons):
        """Press and release the given mouse buttons.
        :param buttons: a bitwise-or'd combination of ``LEFT_BUTTON``,
            ``MIDDLE_BUTTON``, and ``RIGHT_BUTTON``.
        Examples::
            # Click the left button.
            m.click(Mouse.LEFT_BUTTON)
            # Double-click the left button.
            m.click(Mouse.LEFT_BUTTON)
            m.click(Mouse.LEFT_BUTTON)
        """
        self.press(buttons)
        self.release(buttons)

    def move(self, x=0, y=0, wheel=0):
        """Move the mouse and turn the wheel as directed.
        :param x: Move the mouse along the x axis. Negative is to the left, positive
            is to the right.
        :param y: Move the mouse along the y axis. Negative is upwards on the display,
            positive is downwards.
        :param wheel: Rotate the wheel this amount. Negative is toward the user, positive
            is away from the user. The scrolling effect depends on the host.
        Examples::
            # Move 100 to the left. Do not move up and down. Do not roll the scroll wheel.
            m.move(-100, 0, 0)
            # Same, with keyword arguments.
            m.move(x=-100)
            # Move diagonally to the upper right.
            m.move(50, 20)
            # Same.
            m.move(x=50, y=-20)
            # Roll the mouse wheel away from the user.
            m.move(wheel=1)
        """
        # Send multiple reports if necessary to move or scroll requested amounts.
        while x != 0 or y != 0 or wheel != 0:
            partial_x = self._limit(x)
            partial_y = self._limit(y)
            partial_wheel = self._limit(wheel)
            self.report[1] = partial_x & 0xFF
            self.report[2] = partial_y & 0xFF
            self.report[3] = partial_wheel & 0xFF
            self._mouse_device.send_report(self.report)
            x -= partial_x
            y -= partial_y
            wheel -= partial_wheel

    def _send_no_move(self):
        """Send a button-only report."""
        self.report[1] = 0
        self.report[2] = 0
        self.report[3] = 0
        self._mouse_device.send_report(self.report)

    @staticmethod
    def _limit(dist):
        return min(127, max(-127, dist))


m = Mouse(usb_hid.devices)

#m.move(100,0,0)
#time.sleep(0.5)
#m.move(0,100,0)
#time.sleep(0.5)
#m.move(-100,0,0)
#time.sleep(0.5)
#m.move(0,-100,0)

while False:
    time.sleep(60)
    m.move(3,3,0)
    time.sleep(0.2)
    m.move(-3,-3,0)
    time.sleep(0.2)

r = 100

m.move(-int(r/2),0,0)

for i in range(72*8):
    dx = int((math.cos(math.pi*2/72*i)-math.cos(math.pi*2/72*(i+1)))*r)
    dy = int((math.sin(math.pi*2/72*i)-math.sin(math.pi*2/72*(i+1)))*r)
    #print(dx, dy)
    m.move(dx, dy, 0)
    time.sleep(0.01)

m.move(int(r/2),0,0)

