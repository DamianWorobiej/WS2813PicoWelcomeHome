import time
from onboard_led import OnboardLed
from enums import Board, RGB, Battery3p7V
from led_strips import WS2813LedStrip
from inputs import Inputs
from battery_level import BatteryLevelController

STRIP_PIN = 0
SENSOR_INPUT_PIN = 14

BATTERY_INPUT_PIN = 26
RESISTOR_1 = 100000
RESISTOR_2 = 300000
LOW_BATTERY_LEVEL_THRESHOLD = 35.0
LOW_BATTERY_INDICATOR_INDEX = 29

LED_AMOUNT = 30

POST_SIGNAL_LED_DURATION_MS = 20 * 1000
LED_BRIGHTNESS = 0.4

BOARD = Board.PicoZero

strip = WS2813LedStrip(STRIP_PIN, LED_AMOUNT, LOW_BATTERY_INDICATOR_INDEX)

onboardLed = OnboardLed(BOARD)
onboardLed.on()

inputs = Inputs(SENSOR_INPUT_PIN, BATTERY_INPUT_PIN)

battery_level_controller = BatteryLevelController(Battery3p7V(), RESISTOR_1, RESISTOR_2)

signal_timestamp = time.ticks_ms()
signaling = False

while True:
    if inputs.sensor.value() == 1 and signaling is False:
        if inputs.battery_control_enabled is True:
            battery_level_signal = inputs.battery_voltage_signal.read_u16()
            battery_percentage = battery_level_controller.get_battery_percentage(battery_level_signal)

            if battery_percentage <= LOW_BATTERY_LEVEL_THRESHOLD:
                strip.signal_on(RGB.Red)

        signal_timestamp = time.ticks_ms()
        strip.update_all(RGB.White, LED_BRIGHTNESS)
        signaling = True
    elif time.ticks_diff(time.ticks_ms(), signal_timestamp) > POST_SIGNAL_LED_DURATION_MS and signaling is True:
        if inputs.battery_control_enabled is True:
            strip.signal_off()

        strip.update_all(RGB.Off, LED_BRIGHTNESS)
        signaling = False