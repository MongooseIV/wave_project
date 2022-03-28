# from display.oled_display import OledDisplay # TODO: apparently i dont understand how modules work in python
from time import sleep
import turtle
from display.turtle_display import TurtleDisplay

from display.screen import Size
from wave_engine import WaveType
# group width and height

#display = OledDisplay (Size(128, 32) )
display = TurtleDisplay( Size(128, 32), 18, -400 )

def draw_thingy(hz: int):
	sleep(0.05)
	display.turtle.clear()
	display.hertz = hz
	display.draw()
	turtle.update()

	display.turtle.penup()
	display.turtle.goto(display.start_x_offset, 0)
	display.turtle.pendown()


while True:

	for i in range(2, 28):
		draw_thingy(i)

	for i in reversed(range(2, 28)):
		draw_thingy(i)