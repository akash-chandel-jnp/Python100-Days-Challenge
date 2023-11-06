import time
from turtle import Screen
from paddle import Paddle
import ball
from scoreboard import Scoreboard
TIME_LAPSE = .1

screen = Screen()
screen.bgcolor("black")

screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

screen.listen()

# initialization of all the components
r_paddle = Paddle((+350, 0))  # this is how to pass arguments to a class
l_paddle = Paddle((-350, 0))
ball1 = ball.Ball()
scoreboard = Scoreboard()



# Paddle movements controls
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

# ball related codes

# Keep the game running
game_is_on = True
while game_is_on:
    time.sleep(TIME_LAPSE)
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
        TIME_LAPSE *= 0.9

    #r_paddle misses the ball :
    if ball1.xcor() > 380 :
        ball1.reset_position()
        scoreboard.l_point()
        TIME_LAPSE =0.1

    #l_paddle misses the ball :
    if ball1.xcor() < -380 :
        ball1.reset_position()
        scoreboard.r_point()
        TIME_LAPSE =0.1






screen.exitonclick()
