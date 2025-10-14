from picozero import pico_led
import time
from state_machine import StateMachine
from inputs import Inputs
from array import array
    
pico_led.on()

STATE_MACHINE_ID = 0
CONTROLLER_PIN = 0
SENSOR_INPUT_PIN = 16

LED_AMOUNT = 30

POST_SIGNAL_LED_DURATION_MS = 20 * 1000
LED_BRIGHTNESS = 0.4

rgb_white = (255, 255, 255)
rgb_off = (0, 0, 0)

led_array = array("I", range(LED_AMOUNT))        
def update_strip(brightness, color):
    for ii, cc in enumerate(led_array):
        r = int(color[0] * brightness)
        g = int(color[1] * brightness)
        b = int(color[2] * brightness)
        led_array[ii] = (g<<16) + (r<<8) + b
    
    state_machine.put(led_array, 8)

inputs = Inputs(SENSOR_INPUT_PIN)
    
state_machine = StateMachine(STATE_MACHINE_ID, CONTROLLER_PIN)
state_machine.active(1)

update_strip(0, rgb_off)
signal_timestamp = time.ticks_ms()
while True:
    if inputs.sensor.value() == 1:
        signal_timestamp = time.ticks_ms()
        update_strip(LED_BRIGHTNESS, rgb_white)
    elif time.ticks_diff(time.ticks_ms(), signal_timestamp) > POST_SIGNAL_LED_DURATION_MS:
        update_strip(1, rgb_off)