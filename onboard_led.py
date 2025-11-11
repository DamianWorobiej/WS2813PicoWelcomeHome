from machine import Pin
from neopixel import NeoPixel
from enums import Board, RGB

class OnboardLed():
    def __init__(self, board: int = Board.Pico) -> None:
        self.led: LedBase = LedBase()
        if board is Board.Pico:
            self.led = PicoLed()
        if board is Board.PicoZero:
            self.led = PicoZeroLed()

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

class LedBase():
    def on(self):
        pass

    def off(self):
        pass

class PicoZeroLed(LedBase):
    def __init__(self) -> None:
        self.led = NeoPixel(Pin(16), 1)

    def on(self):
        brightness = 0.5
        self.led[0] = ((int)(RGB.White[0] * brightness), (int)(RGB.White[1] * brightness), (int)(RGB.White[2] * brightness))
        self.led.write()

    def off(self):
        self.led[0] = RGB.Off
        self.led.write()

class PicoLed(LedBase):
    def __init__(self) -> None:
        self.led = Pin(25, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)