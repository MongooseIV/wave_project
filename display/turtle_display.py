from turtle import Turtle

from display.screen import Display, Size
import wave_engine
from wave_engine import WaveType

class TurtleDisplay(Display):
	def __init__(self, screen: Size, hertz: int):
		self.screen = screen
		self.hertz = hertz

		self.turtle = Turtle()

	def draw(self) -> None:
		for x in range(0, self.screen.WIDTH):
			print(f"x: {x}")
			self.hertz = 2 if self.hertz < 2 else self.hertz # minimum hz value. should go from 2-28. i forgot why - ssohbn
			y = wave_engine.calculate_wave_point(self.screen, x, self.hertz, wave_type=WaveType.SINE)

			print(f"x: {x}, y: {y}")
			self.turtle.goto(x-100, y)
			self.turtle.pendown()

