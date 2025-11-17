from enums import BaseBattery

class BatteryLevelController():
    def __init__(self, battery: BaseBattery, resistor1: int, resistor2: int) -> None:
        self.__max_readable_voltage: float = 3.3
        self.__signal_max = 65535
        self.__battery: BaseBattery = battery
        self.__voltage_drop_factor: float = (float)(resistor2 / (resistor1 + resistor2))

    def get_battery_percentage(self, voltage_signal: int) -> float:
        current_voltage = voltage_signal * self.__max_readable_voltage / self.__signal_max
        current_source_voltage = current_voltage / self.__voltage_drop_factor

        min_voltage = self.__battery.get_min_voltage()
        max_voltage = self.__battery.get_max_voltage()
        current_percentage = 100 * round(round(current_source_voltage - min_voltage, 4) / round(max_voltage - min_voltage, 4), 2)

        return current_percentage