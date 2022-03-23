# imports
from machine import Pin, I2C, ADC, PWM
from ssd1306 import SSD1306_I2C
import math
from time import sleep

w = 128  # width of screen
h = 32  # height of screen
buzzer = PWM(Pin(13))

# pin assignments
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
addr = i2c.scan()[0]
oled = SSD1306_I2C(w, h, i2c, addr)
adc = ADC(Pin(26))
button = Pin(20, Pin.IN, Pin.PULL_DOWN)
r_led = Pin(16, Pin.OUT)
u_led = Pin(14, Pin.OUT)
g_led = Pin(15, Pin.OUT)

# define vars
x = 0
y = 0
wave_type = "sin"

# reset led
r_led.value(0)
g_led.value(0)
u_led.value(1)


# method definitions
def normalize(a, b):  # changes the hertz value so it is compatible with oled screen size
    return float(b / a)


def toggle_wave(wave):  # changes the wave from sin to cos
    print(wave)
    if wave == "sin":  # when wave is cos, g_led is on
        wave = "cos"
        u_led.value(0)
        g_led.value(1)
    elif wave == "cos":  # when wave is sin, u_led is on
        wave = "sin"
        g_led.value(0)
        u_led.value(1)
    return wave  # returns the correct value


while True:
    for x in range(0, w):
        if button.value():  # checks if the button is pressed
            wave_type = toggle_wave(wave_type)  # switches the type of wave
            sleep(0.5)

        hertz = round((adc.read_u16() / 2340.53571429))  # turns the potentiometer output into 2-28 hertz
        if hertz < 2: hertz = 2  # sets the minumum hertz value
        hertz_as_degrees = math.degrees(math.pi * hertz)  # turns the hertz into degrees of circle
        normalized_x = x * normalize(w, hertz_as_degrees)  # adjusts for small oled screen
        rads_x = math.radians(normalized_x)  # turns degrees into radians
        if wave_type == "sin":
            y = int(math.sin(rads_x) * (h / 2))  # sets y value to sin output
        elif wave_type == "cos":
            y = int(math.cos(rads_x) * (h / 2))  # sets y value to cos output
        oled.pixel(x, y + 16, 1)  # draws waave
        oled.show()
        print(hertz)
        #         print(f"{x}, {y}")
        buzzer.freq(int(hertz * 31.4))
        buzzer.duty_u16(0)
        sleep(0.005)
    oled.fill(0)
