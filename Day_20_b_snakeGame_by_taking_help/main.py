from turtle import Screen
import time
import snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snk = snake.Snake()

food_item = Food()
food_item.forward(20)

score_board1 = Scoreboard()


screen.listen()

screen.onkey(snk.up, "Up")
screen.onkey(snk.down, "Down")
screen.onkey(snk.left, "Left")
screen.onkey(snk.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)  # can also be used to change the speed
    snk.move()

    if snk.head.distance(food_item) < 17:
        print("eaten food")
        food_item.refresh_food()
        snk.extent_snake()
        score_board1.increase_score()

    # TODO : Detect collision with the wall
    if snk.head.xcor() > 280 or snk.head.xcor() < -300 or snk.head.ycor() > 300 or snk.head.ycor() <-280 :
        game_is_on = False
        score_board1.game_over_msg()

    # TODO : Detecting collision of head with the tail
    for segment in snk.segments:
        if segment == snk.head:
            pass
        elif snk.head.distance(segment) < 10:
            game_is_on = False
            score_board1.game_over_msg()
            score_board1.game_over_msg()

screen.exitonclick()
