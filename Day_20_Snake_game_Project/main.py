from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Feed The SNAKE")

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





screen.exitonclick()





