# 1- Create a snake body
# 2- Move the Snake
# 3- Create snake food
# 4- Detect collision with food
# 5- Create a scoreboard
# 6- Detect collision with wall
# 7- Detect collision with tail


import turtle as t
# import time
import snake

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = snake.Snake()








# x = 0
# y = 0
# squares = []
# for s in range(3):
#     each_square = t.Turtle("square")
#     each_square.color("white")
#     each_square.penup()
#     each_square.goto(x=x, y=y)
#     squares.append(each_square)
#     x -= 20

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.5)
#     num_of_squares = len(squares)
#     for n in range(num_of_squares-1, 0, -1):
#         base_cordinate = squares[n - 1].position()
#         squares[n].goto(base_cordinate)
#     squares[0].forward(20)

screen.exitonclick()
