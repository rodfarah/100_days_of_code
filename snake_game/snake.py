import time
from turtle import Screen, Turtle
screen = Screen()

MOVE_DISTANCE = 20
SPEED = 0.1

class Snake:
    def __init__(self) -> None:
        self.squares = []
        self.create_snake()

    def create_snake(self):
        x = 0
        y = 0
        for s in range(3):
            each_square = Turtle("square")
            each_square.color("white")
            each_square.penup()
            each_square.goto(x=x, y=y)
            self.squares.append(each_square)
            x -= 20

    def move(self):
        game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(SPEED)
            num_of_squares = len(self.squares)
            for n in range(num_of_squares-1, 0, -1):
                base_cordinate = self.squares[n - 1].position()
                self.squares[n].goto(base_cordinate)
            self.squares[0].forward(MOVE_DISTANCE)
