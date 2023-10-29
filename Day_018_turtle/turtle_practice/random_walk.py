from turtle import Turtle, Screen
import random

tiro = Turtle()
list_of_color = ["red", "dark khaki", "tomato", "indigo", "dark olive green", "chartreuse", "orange", "dark goldenrod",
                 "purple", "indigo", "olive", "black"]
degrees = [0, 90, 180, 270, 360]
tiro.speed(8)
tiro.width(10)

for _ in range(200):
    tiro.color(random.choice(list_of_color))
    degree = random.choice(degrees)
    tiro.forward(30)
    tiro.setheading(degree)
    # tiro.left(degree)
    # tiro.back(10)

screen = Screen()
screen.exitonclick()
