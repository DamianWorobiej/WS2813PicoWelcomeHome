from machine import Pin
from neopixel import NeoPixel # type: ignore
from led_strips import NeoPixelStrip
from enums import Board, GRB

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
        self.led = NeoPixelStrip(16, 1)

    def on(self):
        brightness = 0.5
        self.led.update_one(GRB.White, brightness, 0)

    def off(self):
        self.led.update_one(GRB.Off, 1, 0)

class PicoLed(LedBase):
    def __init__(self) -> None:
        self.led = Pin(25, Pin.OUT)

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)