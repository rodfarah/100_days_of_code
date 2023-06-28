# 1- Create a snake body
# 2- Move the Snake
# 3- Create snake food
# 4- Detect collision with food
# 5- Create a scoreboard
# 6- Detect collision with wall
# 7- Detect collision with tail

from turtle import Screen
from food import Food
import snake as s
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = s.Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.clear()
        scoreboard.plus_one()
    elif (-280 < snake.head.xcor() > 280) or (-280 < snake.head.ycor() > 280):
        game_is_on = False
        scoreboard.game_over()
    

screen.exitonclick()
