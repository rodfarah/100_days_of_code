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
import ball
import scoreboard as score
import time
from turtle import Screen
from paddle import Paddle, PADDLE_X_POSITION
from net import Net
from random import randint

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

net = Net()

left_paddle = Paddle("left")
right_paddle = Paddle("right")
left_scoreboard = score.Scoreboard((-100, 210))
right_scoreboard = score.Scoreboard((100, 210))

ball = ball.Ball()
ball.first_shot_angle()

screen.listen()
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

pixels = 13
while left_scoreboard.doesnt_win() and right_scoreboard.doesnt_win():
    time.sleep(0.05)
    left_scoreboard.refresh_scoreboard()
    right_scoreboard.refresh_scoreboard()
    screen.update()
    ball.move_on(pixels)

    
    # VARIABLES:
    # Ball touches horizontal edges
    up_wall_kick = (ball.ycor() >= 280)
    down_wall_kick = (ball.ycor() <= -280)

    # Ball touches vertical edges
    left_point = (ball.xcor() > 400)
    right_point = (ball.xcor() < - 400)

    # Ball Transpasses Right Paddle
    btrp = ((PADDLE_X_POSITION +8) > ball.xcor() > (PADDLE_X_POSITION - 20))
    # Ball Transpasses Left Paddle
    btlp = ((-PADDLE_X_POSITION -8) < ball.xcor() < -PADDLE_X_POSITION + 20)

    # Ball kicks UP right Paddle, considering ONLY y coordinates:
    bkurp = (ball.ycor() <= (right_paddle.ycor() + 60) and (ball.ycor() > right_paddle.ycor()))
    # Ball kicks DOWN right Paddle, considering ONLY y coordinates:
    bkdrp = (ball.ycor() >= (right_paddle.ycor() - 60) and (ball.ycor() < right_paddle.ycor()))

    # Ball kicks UP left Paddle, considering ONLY y coordinates:
    bkulp = (ball.ycor() <= (left_paddle.ycor() + 60) and ball.ycor() > left_paddle.ycor())
    # Ball kicks DOWN left Paddle, considering ONLY y coordinates:
    bkdlp = (ball.ycor() >= (left_paddle.ycor() - 60) and ball.ycor() < left_paddle.ycor())

    # Ball kicks walls:
    if up_wall_kick or down_wall_kick:
        ball.horizontal_bounce()

    # Ball kicks Right Paddle:
    elif btrp and ((right_paddle.ycor() - 50) < ball.ycor() < (right_paddle.ycor() + 50)):
        screen.onkey(None, "Up")
        screen.onkey(None, "Down")
        ball.vertical_bounce()
        pixels += 3

    # Ball kicks Left Paddle:
    elif btlp and ((left_paddle.ycor() - 50) < ball.ycor() < (left_paddle.ycor() + 50)):
        screen.onkey(None, "w")
        screen.onkey(None, "s")
        ball.vertical_bounce()
        pixels += 3

    # Ball touches paddles from up or down sides:
    elif all([btrp, bkurp]):
        screen.onkey(None, "Up")
        right_paddle.goto((right_paddle.xcor(), right_paddle.ycor() - 30))
        ball.horizontal_bounce()
    elif all([btrp, bkdrp]):
        screen.onkey(None, "Up")
        right_paddle.goto((right_paddle.xcor(), right_paddle.ycor() + 30))
        ball.horizontal_bounce()
    elif all([btlp, bkulp]):
        screen.onkey(None, "w")
        left_paddle.goto((left_paddle.xcor(), left_paddle.ycor() - 30))
        ball.horizontal_bounce()
    elif all([btlp, bkdlp]):
        screen.onkey(None, "s")
        left_paddle.goto((left_paddle.xcor(), left_paddle.ycor() + 30))
        ball.horizontal_bounce()


    # Scoring points:
    elif right_point:
        right_scoreboard.plus_one()
        ball.goto((0, randint(-280, 280)))
        ball.shooting_angle("right")
        pixels = 13
    elif left_point:
        left_scoreboard.plus_one()
        ball.goto((0, randint(-280, 280)))
        ball.shooting_angle("left")
        pixels = 13

left_scoreboard.and_the_winner_is("LEFT PLAYER", (-200, 0))
right_scoreboard.and_the_winner_is("RIGHT PLAYER", (200, 0))


screen.exitonclick()
