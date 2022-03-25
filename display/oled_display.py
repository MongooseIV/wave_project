
# imports
from display.screen import Display, Size
from machine import Pin, I2C, ADC, PWM
from ssd1306 import SSD1306_I2C
import math
from time import sleep

import wave_engine
from wave_engine import WaveType

class OledDisplay(Display): 
	""" oled display front end """
	def __init__(self, screen: Size):
		self.screen = screen

		# pin assignments
		self.buzzer = PWM(Pin(13))
		self.i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=200000)
		self.addr = self.i2c.scan()[0]
		self.adc = ADC(Pin(26))
		self.button = Pin(20, Pin.IN, Pin.PULL_DOWN)

		self.oled = SSD1306_I2C(self.screen.WIDTH, self.screen.HEIGHT, self.i2c, self.addr)

		# led pin assignments
		r_led = Pin(16, Pin.OUT)
		g_led = Pin(15, Pin.OUT)
		u_led = Pin(14, Pin.OUT)

		# reset leds
		r_led.value(0) 
		g_led.value(0)
		u_led.value(1)

		self.wave_type = WaveType.SINE # default wave type
	

		def draw(self, screen: Size) -> None:
			for x in range(0, screen.WIDTH):
				if self.button.value():  # checks if the button is pressed
					self.wave_type = wave_engine.toggle_wave(self.wave_type)  # switches the type of wave
					sleep(0.5)

				hertz = round((self.adc.read_u16() / 2340.53571429))  # turns the potentiometer output into 2-28 hertz
				# TODO: get rid of magic number. u16 is the 655189 number or something i forgot 

				hertz = 2 if hertz < 2 else hertz # minimum hz value. should go from 2-28. i forgot why - ssohbn

				y = wave_engine.calculate_wave_point(screen, x, hertz, wave_type=self.wave_type)

				self.oled.pixel(x, y + 16, 1)  # draws waave
				self.oled.show()
				print(hertz)
				#         print(f"{x}, {y}")
				self.buzzer.freq(int(hertz * 31.4))
				self.buzzer.duty_u16(0)
				sleep(0.005)
			self.oled.fill(0)

