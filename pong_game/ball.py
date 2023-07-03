from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(randint())
        self.penup()


    def move_on(self):
        self.forward(10)

    def wall_bounce(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.setheading(180 - self.heading())
