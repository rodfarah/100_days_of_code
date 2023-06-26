# 10 by 10
# Each dot 20 size and spaced apart by around 50 paces

import turtle
import random

turtle.colormode(255)


def random_color() -> tuple[int, int, int]:
    """Return a tuple containing r, g, b color items from a color list"""
    color_list = [(133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98), (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102), (175, 185, 215),
                  (21, 168, 123), (161, 209, 166), (174, 154, 74), (3, 96, 115), (237, 161, 174), (238, 166, 152), (54, 59, 93), (152, 207, 220), (102, 126, 174), (40, 56, 76), (34, 87, 53), (232, 209, 16), (74, 79, 40)]
    return random.choice(color_list)


hirst = turtle.Turtle()

hirst.shape("arrow")

size = 20
x = -200
y = -200

for t in range(10):
    hirst.penup()
    hirst.setpos(x, y)
    for n in range(10):
        hirst.dot(size, random_color())
        hirst.penup()
        hirst.fd(50)
    y += 50

hirst.hideturtle()

ts = turtle.Screen()
turtle.exitonclick()
