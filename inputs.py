from machine import Pin

class Inputs:
    def __init__(self, sensor_pin_number):
      self.sensor = Pin(sensor_pin_number, Pin.IN)