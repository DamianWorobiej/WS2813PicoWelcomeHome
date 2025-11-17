from machine import Pin
from lowpower import dormant_until_pin, lightsleep
from enums import Board

class PowerSaver:
    def __init__(self, wake_up_pin_number: int) -> None:
        self.__wake_up_pin_number = wake_up_pin_number
        self.__wake_up_pin: Pin = Pin(wake_up_pin_number)
  
    def deep_sleep(self) -> None:
        pass

    def light_sleep(self) -> None:
        pass

class PicoPowerSaver(PowerSaver):
    def __init__(self, wake_up_pin_number: int) -> None:
        super().__init__(wake_up_pin_number)

    def deep_sleep(self) -> None:
        dormant_until_pin(self.__wake_up_pin_number, False, True)

    def light_sleep(self) -> None:
        lightsleep()

class PowerSaverFactory:
    @staticmethod
    def create(board_id: int, wake_up_pin_number: int) -> PowerSaver | None:
        if board_id is Board.Pico or Board.PicoZero:
            return PicoPowerSaver(wake_up_pin_number)
        
        return None