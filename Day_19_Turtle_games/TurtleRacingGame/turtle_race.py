from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)


#compulsarily taking user bet
user_bet = False
isRaceOn = False
while not user_bet:
    user_bet = screen.textinput("Make Your Bet", "Which color turtle will win ? ").lower()
    if user_bet:
        isRaceOn = True
    else:
        isRaceOn = False

# print(user_bet)
colors = ["red", "green", "yellow", "orange", "purple", "blue"]
y = -100

all_turtles = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(-230, y)
    y += 30
    all_turtles.append(tim)


while isRaceOn:
    for tim in all_turtles:
        tim.forward(random.randint(0,10))
        if tim.pos()[0] >= +230:

            if tim.pencolor() == user_bet:
                print(f"You WIN ! {tim.pencolor()} won the race !")
            else:
                print(f"You LOSE ! {tim.pencolor()} won the race !")
            isRaceOn = False

screen.exitonclick()
