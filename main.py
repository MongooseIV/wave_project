from display.oled_display import OledDisplay
from display.screen import Size
from wave_engine import WaveType
# group width and height

display = OledDisplay (Size(128, 32) )

while True:
    display.draw()