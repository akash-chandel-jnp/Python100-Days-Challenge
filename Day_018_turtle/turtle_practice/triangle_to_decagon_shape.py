from turtle import Turtle, Screen
import random

tur = Turtle()
list_of_color = ["red", "dark khaki", "tomato", "indigo", "dark olive green", "chartreuse", "orange", "dark goldenrod", "purple", "indigo", "olive", "black"]

# for i in range(3, 11):
#     tur.color(random.choice(list_of_color))
#     angle = 360 / i
#     for j in range(i):
#         tur.forward(100)
#         tur.right(angle)


def draw_shape(num_of_edges):
    tur.color(random.choice(list_of_color))
    ext_angle = 360 / num_of_edges
    for j in range(num_of_edges):
        tur.forward(100)
        tur.right(ext_angle)


for n in range(3, 11):
    draw_shape(n)

screen = Screen()
screen.exitonclick()
