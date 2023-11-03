from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snk = snake.Snake()

screen.listen()

screen.onkey(snk.up, "Up")
screen.onkey(snk.down, "Down")
screen.onkey(snk.left, "Left")
screen.onkey(snk.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snk.move()


for seg_num in range(len(segments) - 1, 0, -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()

    segments[seg_num].goto(new_x, new_y)
segments[0].forward(20)
# segments[0].left(90)

screen.exitonclick()
