from turtle import Screen
import time
from car_managing import Car
from pedestrian import Pedestrian
from random import choice
screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

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


screen.exitonclick()
