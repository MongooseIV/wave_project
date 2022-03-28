from tracemalloc import start
from turtle import Turtle
import turtle
from time import sleep

from display.screen import Display, Size
import wave_engine
from wave_engine import WaveType

class TurtleDisplay(Display):
	def __init__(self, screen: Size, hertz: int, start_x_offset: int):
		self.screen = screen
		self.hertz = hertz
		# offset because turtle decides to start in the middle
		self.start_x_offset = start_x_offset 

		self.turtle = Turtle()
		self.turtle.speed(0)
		self.turtle.hideturtle()

		self.turtle.penup()
		self.turtle.goto(self.start_x_offset, 0)
		self.turtle.pendown()

	def draw(self) -> None:
		sleep(0.05)
		self.turtle.clear()

		turtle.tracer(0,0)
		for x in range(0, self.screen.WIDTH):
			# self.hertz = 2 if self.hertz < 2 else self.hertz # minimum hz value. should go from 2-28. i forgot why - ssohbn
			y = wave_engine.calculate_wave_point(self.screen, x, self.hertz, wave_type=WaveType.SINE)

			self.turtle.goto(x+self.start_x_offset, y)
			self.turtle.pendown()

		turtle.update()

