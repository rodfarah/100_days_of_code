
from turtle import Screen
from food import Food
import snake as s
import time
from scoreboard import Scoreboard

WALLCRASH = 295  # pixels


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
    x_crashes = snake.head.xcor() < - WALLCRASH or snake.head.xcor() > WALLCRASH
    y_crashes = snake.head.ycor() < - WALLCRASH or snake.head.ycor() > WALLCRASH

    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.clear()
        scoreboard.plus_one()
        bite_coord = snake.squares[-1].position()
        snake.add_square(bite_coord)
    elif any((x_crashes, y_crashes)):
        scoreboard.reset()
        snake.snake_crashes()
    
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            scoreboard.reset()
            snake.snake_crashes()



screen.exitonclick()
