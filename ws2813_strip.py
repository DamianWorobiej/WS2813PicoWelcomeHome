from neopixel import NeoPixel
from machine import Pin

class LedStrip():
    def __init__(self, pin: Pin, led_count: int, signal_diode_index: int | None = None) -> None:
        self.led_array = NeoPixel(pin, led_count)
        self.signaling_set_up = signal_diode_index is not None
        self.signal_diode_index = signal_diode_index
        self.signaling = False
        self.old_color = (0, 0, 0)

    def update_all(self, color: tuple, brightness: float) -> None:
        new_color = ((int)(color[0] * brightness), (int)(color[1] * brightness), (int)(color[2] * brightness))
        for index, value in enumerate(self.led_array):
            if self.signaling_set_up is True:
                if self.signaling is True and index == self.signal_diode_index:
                    continue

            self.led_array[index] = new_color

        self.old_color = new_color
        self.led_array.write()

    def signal_on(self, color: tuple) -> None:
        if self.signaling_set_up is True and self.signaling is False:
            self.old_color = self.led_array[0]
            self.signaling = True
            self.led_array[self.signal_diode_index] = color
            self.led_array.write()

    def signal_off(self) -> None:
        if self.signaling_set_up is True and self.signaling is True:
            self.signaling = False
            self.update_all(self.old_color, 1)