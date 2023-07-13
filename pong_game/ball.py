from turtle import Turtle
from random import randint, choice

SHUFFLE_ANGLE_VARIATION = 20
SIDES = ["left", "right"]
LEFT_STARTING_ANGLES = [125, 215]
RIGHT_STARTING_ANGLES = [305, 35]


class Ball(Turtle):
    """Instanciate a ball object"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def first_shot_angle(self):
        """Define shooting angle at first, when game is on."""
        self.shooting_angle(choice(SIDES))

    def shooting_angle(self, side: str) -> int:
        """Return shooting angle, excluding too horizontal or too vertical ones."""
        random_options = []
        if side == "right":
            for angle in RIGHT_STARTING_ANGLES:
                random_options.append(randint(angle, angle + SHUFFLE_ANGLE_VARIATION))
            self.setheading(choice(random_options))
        elif side == "left":
            for angle in LEFT_STARTING_ANGLES:
                random_options.append(randint(angle, angle + SHUFFLE_ANGLE_VARIATION))
            self.setheading(choice(random_options))

    def move_on(self, pixels: int):
        """Move object on"""
        self.forward(pixels)

    def horizontal_bounce(self):
        """Set heading of an object when it bounces up or down screen."""
        self.setheading(360 - self.heading())

    def vertical_bounce(self):
        """Set heading of an object when it bounces paddles."""
        if 0 < self.heading() < 180:
            self.setheading(180 - self.heading())
        elif 180 < self.heading() < 360:
            self.setheading(360 - (self.heading() - 180))
