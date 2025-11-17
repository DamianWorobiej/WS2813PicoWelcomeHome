class Board:
    Pico = 1
    PicoZero = 2

class RGB:
    Off = (0, 0, 0)
    White = (255, 255, 255)
    Red = (255, 0, 0)
    Green = (0, 255, 0)
    Blue = (0, 0, 255)

class GRB:
    Off = (0, 0, 0)
    White = (255, 255, 255)
    Red = (0, 255, 0)
    Green = (255, 0, 0)
    Blue = (0, 0, 255)

class BaseBattery:
    def __init__(self) -> None:
        self.__max_voltage = 0
        self.__min_voltage = 0
        self.__rated_voltage = 0

    def get_max_voltage(self) -> float:
        return self.__max_voltage
    
    def get_min_voltage(self) -> float:
        return self.__min_voltage
    
    def get_rated_voltage(self) -> float:
        return self.__rated_voltage

class Battery3p7V(BaseBattery):
    def __init__(self) -> None:
        super().__init__()
        self.__max_voltage = 4.2
        self.__min_voltage = 2.5
        self.__rated_voltage = 3.7