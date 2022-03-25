from turtle import width


class Size:
    """ datatype to group width and height together """
    def __init__(self, WIDTH: int, HEIGHT: int):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

class Display:
    def __init__(self, screen: Size):
        self.screen = screen

    def draw(self) -> None: # displays need a way to display
        pass
