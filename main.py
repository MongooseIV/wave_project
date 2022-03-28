# from display.oled_display import OledDisplay # TODO: apparently i dont understand how modules work in python
import turtle
from display.turtle_display import TurtleDisplay

from display.screen import Size
from wave_engine import WaveType
# group width and height

# display = OledDisplay (Size(128, 32) )
display = TurtleDisplay( Size(640, 300), 18, -400 )

def draw_thingy(hz: int):
	display.hertz = hz
	display.draw()


while True:

	for i in range(2, 28):
		draw_thingy(i)

	for i in reversed(range(2, 28)):
		draw_thingy(i)