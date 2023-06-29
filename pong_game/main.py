"""
- Create Screen with a Net
- Create Paddle class (4 vertical squares) and move it.
- Create another Paddle
- Create Ball class and shoot it.
- Detect ball hitting and bouncing walls
- Detect ball hiting Paddle.
- Detect ball missing Paddle backyards.
- Create a Scoreboard class (create numbers made of squares), increase scoreboard's opponent in 1 point.
"""

from turtle import Screen, Turtle
from net import Net

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

net = Net()

net.whole_net()

screen.exitonclick()