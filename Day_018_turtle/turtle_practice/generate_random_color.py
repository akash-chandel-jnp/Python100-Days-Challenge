import turtle as t
from turtle import Screen
import random

# Changing the color mode from within the module itself
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, b, g)
    return random_colour


turr = t.Turtle()

degrees = [0, 90, 180, 270, 360]
turr.speed(8)
turr.width(10)

for _ in range(100):
    turr.color(random_color())

    # turr.color(random_color()[0], random_color()[1], random_color()[2])
    degree = random.choice(degrees)
    turr.forward(30)
    turr.setheading(degree)
    # turr.left(degree)
    # turr.back(10)

screen = Screen()
screen.exitonclick()
