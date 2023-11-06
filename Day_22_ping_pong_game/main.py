from turtle import Turtle, Screen
from sliders import Slider

screen = Screen()
screen.setup(1800, 800)
screen.bgcolor("black")
screen.tracer(0)

slider1 = Slider()

game_is_on = True

while game_is_on:
    screen.listen()
    screen.onkeypress(slider1.up, "Up")
    screen.onkeypress(slider1.down, "Down")

    screen.update()
screen.exitonclick()
