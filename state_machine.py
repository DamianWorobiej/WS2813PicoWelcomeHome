import rp2
from rp2 import PIO, asm_pio
from rp2 import StateMachine as BaseStateMachine
from machine import Pin

class StateMachine():
    def __init__(self, machine_id, pin_number):
        self.__machine = BaseStateMachine(machine_id, self.__strip_setup, freq=8000000, sideset_base=Pin(pin_number) )
    
    def active(self, value):
        self.__machine.active(value)
        
    def put(self, value, bits):
        self.__machine.put(value, bits)
    
    @asm_pio(sideset_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
    def __strip_setup():
        T1 = 2
        T2 = 5
        T3 = 3
        label("bitloop")
        out(x, 1).side(0)[T3-1]
        jmp(not_x, "do_zero").side(1)[T1-1]
        jmp("bitloop").side(1)[T2-1]
        label("do_zero")
        nop().side(0)[T2-1]