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
from turtle import Screen
from paddle import Paddle
from net import whole_net
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height=600)
screen.tracer(0)
whole_net()

left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_on()
    
    if any([ball.xcor() < - 400, ball.xcor() > 400]):
        game_is_on = False
    elif ball.distance(right_paddle) < 50 and ball.xcor() > 325:
        ball.paddle_bounce()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -325:
        ball.paddle_bounce()
    elif any([ball.ycor() >= 280, ball.ycor() <= -280]):
        ball.wall_bounce()

screen.exitonclick()