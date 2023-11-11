import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)





# Managing screen to not exit when clicked on screen
turtle.mainloop() # this is an alternative to exitonclick function --> this does not exitonclick -> and we need this as we have to click on the screen to know its coordinates
# screen.exitonclick()