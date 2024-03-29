from turtle import Turtle


class Pedestrian(Turtle):
    """Instantiate a turtle object, the one who will cross the road."""

    def __init__(self, speed=10, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.speed = speed
        self.color("black")
        self.penup()
        self.goto(0, -290)
        self.setheading(90)

    def move_up(self):
        """Move up the turtle object"""
        self.forward(self.speed)
