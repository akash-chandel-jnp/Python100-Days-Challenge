import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)



user_guess = screen.textinput("Guess state name" , "Guess the name of the State in US")


# Convert the csv of the states names into a dataframe
import pandas as pd
data = pd.read_csv('./50_states.csv')
print(data)



for i in range(len(data)):
    if user_guess == data.state[i]:
        details = (i , data.x[i] , data.y[i])
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto((details[1], details[2]))
        t.write(f"{user_guess}")
    # print(data.state)






# # Do something to get the coordinates of the points where mouse is clicked.
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# Managing screen to not exit when clicked on screen
turtle.mainloop()  # this is an alternative to exitonclick function --> this does not exitonclick -> and we need this as we have to click on the screen to know its coordinates
# screen.exitonclick()
