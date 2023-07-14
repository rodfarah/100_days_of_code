from turtle import Screen
import time
from car_managing import Car
from pedestrian import Pedestrian
from random import choice
import level

screen = Screen()
screen.title("Turtle Crossing Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = level.Level()
pedestrian = Pedestrian(speed=10)
car = Car()

screen.listen()

screen.onkeypress(pedestrian.move_up, "Up")


instantiate_car = ["yes", "no"]

game_is_on = True
pixel_speed = 10
car.create_first_car()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if choice(instantiate_car) == "yes":
        car.create_another_car()
    car.move_left(pixel_speed)
    for y_cord in car.possible_colision():
        if (y_cord + 20) > pedestrian.ycor() > (y_cord - 28):
            scoreboard.game_over()
            game_is_on = False
    if pedestrian.ycor() >= 310:
        scoreboard.clear()
        pixel_speed += 3
        scoreboard.increase_level()
        pedestrian.goto(0, -290)

screen.exitonclick()
