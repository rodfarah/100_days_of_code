# w = Forwards
# s = Backwards
# a = Counter-Clockwise
# d = Clockwise
# c = Clear drawing

from turtle import Turtle, Screen
bruna = Turtle()
screen = Screen()


def move_forwards():
    bruna.forward(10)


def move_backwards():
    bruna.backward(10)


def turn_right():
    bruna.right(10)


def turn_left():
    bruna.left(10)


def clear():
    bruna.clear()
    bruna.penup()
    bruna.home()
    bruna.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(clear, "c")

screen.exitonclick()
