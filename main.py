import random
import utime
from machine import Pin


green_led = Pin("LED", Pin.OUT)
red_led = Pin(22, Pin.OUT)
yellow_led = Pin(9, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)
pressed = False


def button_handler(pin):
    utime.sleep_ms(100)
    if pin.value() == 1:
        global pressed
        if not pressed:
            pressed = True
            heads_or_tails()
            pressed = False


def random_led():
    rand = random.randint(0, 1)
    if rand == 0:
        return red_led
    else:
        return yellow_led


def alternately_flash_leds(end_ms=400, increment=20):
    red_led.high()
    i = 50
    while i < end_ms:
        utime.sleep_ms(i)
        i = i + increment
        red_led.toggle()
        yellow_led.toggle()


def flash_winner(led, interval=250):
    for x in range(7):
        led.toggle()
        utime.sleep_ms(interval)


def heads_or_tails():
    reset()
    led = random_led()
    alternately_flash_leds()
    reset()
    flash_winner(led)


def reset():
    red_led.low()
    yellow_led.low()


green_led.high()
reset()
button.irq(trigger=Pin.IRQ_RISING, handler=button_handler)

