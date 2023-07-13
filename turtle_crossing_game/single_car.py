from turtle import Turtle
from random import choice


COLORS = ["orange", "blue", "green", "yellow", "grey", "red", "purple"]

LOWER_Y_POS = -260
HIGHER_Y_POS = 280
GAP_BT_CARS = 5


def possible_position(lower_y=LOWER_Y_POS, higher_y=HIGHER_Y_POS) -> tuple[int, int]:
    """Return a tuple with x (310 fixed) and y (shuffled) coordinates"""
    y_pos = LOWER_Y_POS
    initial_y = []
    while y_pos <= HIGHER_Y_POS:
        initial_y.append(y_pos)
        y_pos += (20 + GAP_BT_CARS)
    return (310, choice(initial_y))

class SingleCar(Turtle):
    def __init__(self, shape: str = "square", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shapesize(1, 2)
        self.penup()
        self.color(choice(COLORS))