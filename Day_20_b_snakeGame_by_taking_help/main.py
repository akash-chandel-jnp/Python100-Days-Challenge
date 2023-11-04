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
    time.sleep(.1)
    snk.move()

    if snk.head.distance(food_item) < 17:
        print("eaten food")
        food_item.refresh_food()
        score_board1.increase_score()

screen.exitonclick()
