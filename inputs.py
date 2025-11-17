from machine import Pin, ADC

class Inputs:
    def __init__(self, sensor_pin_number: int, battery_level_controller_pin_number: int | None = None):
      self.sensor: Pin = Pin(sensor_pin_number, Pin.IN)
      self.battery_control_enabled = False
      if battery_level_controller_pin_number is not None:
        self.battery_control_enabled = True
        self.battery_voltage_signal: ADC = ADC(Pin(battery_level_controller_pin_number))