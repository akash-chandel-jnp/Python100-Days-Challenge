from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("orange")

for _ in range(0, 4):
    tim.forward(100)
    tim.left(90)

screen = Screen()
screen.exitonclick()

for steps in range(100):
    for c in ("blue", "red", "green"):
        tim.color(c)
        tim.forward(steps)
        tim.right(30)