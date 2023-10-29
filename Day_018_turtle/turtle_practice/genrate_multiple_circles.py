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


turd = t.Turtle()

turd.speed('fastest')
turd.width(3)


def draw_spiral(radius, gap):
    for _ in range(int(360 / gap)):
        random_color()
        turd.color(random_color())
        turd.circle(radius)
        turd.left( gap)  # This will move the direction of the head of the turtle by a "gap" degree every time a circle is complete
        # we could also use heading to change direction


draw_spiral(100, 3)

screen = Screen()
screen.exitonclick()
