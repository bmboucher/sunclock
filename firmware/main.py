# main.py -- put your code here!

from machine import Pin, Timer

led = Pin("LED", Pin.OUT)
timer = Timer()

def blink(timer: Timer):
    led.toggle()

timer.init(freq=4, mode=Timer.PERIODIC, callback=blink)