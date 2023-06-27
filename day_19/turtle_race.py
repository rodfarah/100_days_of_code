from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]

user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter one of the rainbow color: ")

all_turtles = []
y = -100
for n in range(6):
    each_turtle = Turtle(shape="turtle")
    each_turtle.color(turtle_colors[n])
    each_turtle.penup()
    each_turtle.goto(x=-230, y=y)
    all_turtles.append(each_turtle)
    y += 30

race_is_on = True
while race_is_on:
    for turtle_moving in all_turtles:
        turtle_moving.forward(random.randint(0, 10))
        if turtle_moving.xcor() > 230:
            winner_color = turtle_moving.pencolor()
            race_is_on = False


print(f"{winner_color} turtle wins the race!")
if user_bet == winner_color:
    print("You WON!")
else:
    print("You've LOST!")

screen.exitonclick()
