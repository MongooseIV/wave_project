from display.oled_display import OledDisplay # TODO: apparently i dont understand how modules work in python
from display.turtle_display import TurtleDisplay

from display.screen import Size
from wave_engine import WaveType
# group width and height

# display = OledDisplay (Size(128, 32) )
display = TurtleDisplay( Size(128, 32), 12 )

while True:
	display.draw()