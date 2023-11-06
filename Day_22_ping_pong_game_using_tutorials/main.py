from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")

screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

screen.listen()

r_paddle = Paddle((+350,0))
l_paddle = Paddle((-350,0))

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")


screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on :
    screen.update()


screen.exitonclick()
