import math
from tkinter import W
from display.screen import Size

from enum import Enum

class WaveType(Enum):
	""" currently supported wave types """
	SINE = 0
	COSINE = 1

# method definitions
def normalize(a, b) -> float:  # changes the hertz value so it is compatible with oled screen size
	return float(b / a)

def toggle_wave(wave: WaveType) -> WaveType:  # toggles between sine and cosine wave types
	print(wave)
	if wave == WaveType.SINE:  # when wave is cos, g_led is on
		wave = WaveType.COSINE
	elif wave == WaveType.COSINE:  # when wave is sin, u_led is on
		wave = WaveType.SINE
	return wave  # returns the correct value

def calculate_wave_point(screen: Size, x: int, hertz: int, wave_type = WaveType.SINE) -> int:
	""" 
	TODO: read this and do something about it
	hertz should be between 2-28. i do not know why but it is a limit in the previous code
	 - i think it was to make sure all possible waves on the oled were wavy looking?

	wave_type defaults to a sine wave.
	x is the horizontal point to find a funky value for. 
	hertz is the frequency of the sine wave thing
	screen is needed to remap the sine wave to work on a awesome looking oled screen
	"""

	hertz_as_degrees = math.degrees(math.pi * hertz)  # turns the hertz into degrees of circle
	normalized_x = x * normalize(screen.WIDTH, hertz_as_degrees)  # adjusts for small oled screen
	rads_x = math.radians(normalized_x)  # turns degrees into radians

	# TODO: this broke asf

	y = 0
	if wave_type == WaveType.SINE:
		y = int(math.sin(rads_x) * (screen.HEIGHT / 2))  # sets y value to sin output

	elif wave_type == WaveType.COSINE:
		y = int(math.cos(rads_x) * (screen.HEIGHT / 2))  # sets y value to cos output

	return y