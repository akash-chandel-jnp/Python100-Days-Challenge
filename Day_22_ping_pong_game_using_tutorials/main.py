import time
from turtle import Screen
from paddle import Paddle
import ball

screen = Screen()
screen.bgcolor("black")

screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

screen.listen()

# paddle creation
r_paddle = Paddle((+350, 0))  # this is how to pass arguments to a class
l_paddle = Paddle((-350, 0))

# Paddle movements controls
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# ball related codes
ball1 = ball.Ball()

# Keep the game running
game_is_on = True
while game_is_on:
    time.sleep(.05)
    screen.update()
    ball1.move()

    # detect a collision with the upper or lower wall
    if ball1.ycor() > 280 or ball1.ycor() < -280:
        # Bounce the ball
        ball1.bounce_from_wall()

    # detect collision with the paddle
    if ball1.distance(r_paddle) < 50 and ball1.xcor() > 320  or ball1.distance(l_paddle) < 50 and ball1.xcor() < -320:
     # Bounce from paddle
        ball1.bounce_from_paddle()



screen.exitonclick()
