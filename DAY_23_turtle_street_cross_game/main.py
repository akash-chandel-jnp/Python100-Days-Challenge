from turtle import Screen
from cars import Car
import time
import random
from pedestrian import Pedestrian

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Turtle Crossing The Road")
screen.tracer(0)

screen.listen()

list_of_cars = []

the_turtle = Pedestrian()
screen.onkey(the_turtle.move_up, "Up")
screen.onkey(the_turtle.move_down, "Down")


no_of_cars = random.randint(15, 40)
# for i in range(no_of_cars):

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.2)
    random_x = random.randrange(400, 600, 150)
    random_y = random.randrange(-280, 280, 60)
    car = Car((random_x, random_y))
    list_of_cars.append(car)

    for c in list_of_cars:
        c.car_move()


screen.exitonclick()
