# imports
from machine import Pin, I2C, ADC, PWM
from ssd1306 import SSD1306_I2C
import math
from time import sleep

from screen import Size
from wave_engine import WaveType

import wave_engine

# group width and height
screen = Size(128, 32)


# pin assignments
buzzer = PWM(Pin(13))
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
addr = i2c.scan()[0]
oled = SSD1306_I2C(screen.WIDTH, screen.HEIGHT, i2c, addr)
adc = ADC(Pin(26))
button = Pin(20, Pin.IN, Pin.PULL_DOWN)

# led pin assignments
r_led = Pin(16, Pin.OUT)
u_led = Pin(14, Pin.OUT)
g_led = Pin(15, Pin.OUT)

# define vars
x = 0
y = 0
wave_type = WaveType.SINE # default wave type

# reset leds
r_led.value(0) 
g_led.value(0)
u_led.value(1)


def draw(screen: Size) -> None:
    for x in range(0, screen.WIDTH):
        if button.value():  # checks if the button is pressed
            wave_type = wave_engine.toggle_wave(wave_type)  # switches the type of wave
            sleep(0.5)
        hertz = round((adc.read_u16() / 2340.53571429))  # turns the potentiometer output into 2-28 hertz
        # TODO: get rid of magic number. u16 is the 655189 number or something i forgot 

        hertz = 2 if hertz < 2 else hertz # minimum hz value. should go from 2-28. i forgot why - ssohbn

        y = wave_engine.calculate_wave_point(screen, x, hertz, wave_type=wave_type)

        oled.pixel(x, y + 16, 1)  # draws waave
        oled.show()
        print(hertz)
        #         print(f"{x}, {y}")
        buzzer.freq(int(hertz * 31.4))
        buzzer.duty_u16(0)
        sleep(0.005)
    oled.fill(0)

while True:
    draw(screen)