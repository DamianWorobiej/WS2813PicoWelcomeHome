from neopixel import NeoPixel # type: ignore
from machine import Pin
from state_machine import StateMachine
from array import array

class LedStrip():
    def __init__(self, pin_number: int, led_count: int, signal_diode_index: int | None = None) -> None:
        pass

    def update_all(self, color: tuple, brightness: float) -> None:
        pass

    def update_one(self, color: tuple, brightness: float, index: int) -> None:
        pass

    def signal_on(self, color: tuple) -> None:
        pass

    def signal_off(self) -> None:
        pass

class WS2813LedStrip(LedStrip):
    def __init__(self, pin_number: int, led_count: int, signal_diode_index: int | None = None) -> None:
        super().__init__(pin_number, led_count, signal_diode_index)
        self.__state_machine = StateMachine(0, pin_number)
        self.__state_machine.active(1)
        self.__led_array = array("I", range(led_count))
        self.signaling_set_up = signal_diode_index is not None
        self.__signal_diode_index: int = signal_diode_index if signal_diode_index is not None else -1
        self.__signaling = False
        self.__old_color = (0, 0, 0)

    def update_all(self, color: tuple, brightness: float) -> None:
        new_color = tuple((int)(x * brightness) for x in color)
        for index, _ in enumerate(self.__led_array):
            if self.signaling_set_up is True:
                if self.__signaling is True and index == self.__signal_diode_index:
                    continue

            self.__led_array[index] = self.__convert_color_to_number(new_color)

        self.__old_color = new_color
        self.__commit_strip_update()

    def update_one(self, color: tuple, brightness: float, index: int) -> None:
        self.__led_array[index] = self.__convert_color_to_number(color, brightness)
        self.__commit_strip_update()

    def signal_on(self, color: tuple) -> None:
        if self.signaling_set_up is True and self.__signaling is False:
            self.__old_color = self.__led_array[self.__signal_diode_index]
            self.__signaling = True
            self.update_one(color, 1, self.__signal_diode_index)

    def signal_off(self) -> None:
        if self.signaling_set_up is True and self.__signaling is True:
            self.__signaling = False
            self.update_one(self.__old_color, 1, self.__signal_diode_index)

    def __convert_color_to_number(self, color: tuple, brightness: float | None = None):
        if brightness is not None:
            return ((color[1] * brightness)<<16) + ((color[0] * brightness)<<8) + color[2] * brightness
        return (color[1]<<16) + (color[0]<<8) + color[2]

    def __commit_strip_update(self):
        self.__state_machine.put(self.__led_array, 8)

class NeoPixelStrip(LedStrip):
    def __init__(self, pin_number: int, led_count: int, signal_diode_index: int | None = None) -> None:
        super().__init__(pin_number, led_count, signal_diode_index)
        self.__led_array = NeoPixel(Pin(pin_number), led_count)
        self.signaling_set_up = signal_diode_index is not None
        self.__signal_diode_index = signal_diode_index
        self.__signaling = False
        self.__old_color = (0, 0, 0)

    def update_all(self, color: tuple, brightness: float) -> None:
        new_color = tuple((int)(x * brightness) for x in color)
        for index, _ in enumerate(self.__led_array):
            if self.signaling_set_up is True:
                if self.__signaling is True and index == self.__signal_diode_index:
                    continue

            self.__led_array[index] = new_color

        self.__old_color = new_color
        self.__led_array.write()

    def update_one(self, color: tuple, brightness: float, index: int) -> None:
        self.__led_array[index] = tuple((int)(x * brightness) for x in color)
        self.__led_array.write()

    def signal_on(self, color: tuple) -> None:
        if self.signaling_set_up is True and self.__signaling is False:
            self.__old_color = self.__led_array[self.__signal_diode_index]
            self.__signaling = True
            self.__led_array[self.__signal_diode_index] = color
            self.__led_array.write()

    def signal_off(self) -> None:
        if self.signaling_set_up is True and self.__signaling is True:
            self.__signaling = False
            self.update_all(self.__old_color, 1)