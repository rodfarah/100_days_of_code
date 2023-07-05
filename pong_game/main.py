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
import ball
import scoreboard as score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
whole_net()

left_paddle = Paddle("left")
right_paddle = Paddle("right")
left_scoreboard = score.Scoreboard((-100, 210))
right_scoreboard = score.Scoreboard((100, 210))
ball = ball.Ball()
ball.first_shot_angle()

screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")


pixels = 10
while left_scoreboard.doesnt_win() and right_scoreboard.doesnt_win():
    time.sleep(0.05)
    left_scoreboard.refresh_scoreboard()
    right_scoreboard.refresh_scoreboard()
    screen.update()
    ball.move_on(pixels)

    if ball.xcor() < - 400:
        right_scoreboard.plus_one()
        ball.home()
        ball.shooting_angle("right")
        pixels = 10
    elif ball.xcor() > 400:
        left_scoreboard.plus_one()
        ball.home()
        ball.shooting_angle("left")
        pixels = 10
    elif ball.distance(right_paddle) < 100 and ball.xcor() > 325:
        ball.paddle_bounce()
        pixels += 5
    elif ball.distance(left_paddle) < 100 and ball.xcor() < -325:
        ball.paddle_bounce()
        pixels += 5
    elif any([ball.ycor() >= 280, ball.ycor() <= -280]):
        ball.wall_bounce()

left_scoreboard.and_the_winner_is("LEFT PLAYER", (-200, 0))
right_scoreboard.and_the_winner_is("RIGHT PLAYER", (200, 0))


screen.exitonclick()
