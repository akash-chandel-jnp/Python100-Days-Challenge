from turtle import Turtle, Screen
from screen_listener import head_east, head_west, head_north, head_south

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Feed The SNAKE")
screen.listen()


# TODO 1: create 3 turtles
initial_x = 0
initial_y = 0
all_turtles = []
for i in range(3):
    tur = Turtle(shape="square")
    tur.color("white")
    tur.penup()
    tur.setposition(initial_x, initial_y)
    all_turtles.append(tur)
    initial_x += 20


screen.onkey(lambda :head_north(tur), "Up")
screen.onkey(lambda :head_west(tur), "Left")
screen.onkey(lambda :head_east(tur), "Right")
screen.onkey(lambda :head_south(tur), "Down")



screen.exitonclick()





