import turtle
from turtle import Turtle, Screen

import pandas

screen = Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


# At the bottom of the map , inform user that to exit the game he can type 'Exit' : then while loop will break and screen will exit automatically
exit_msg = Turtle()
exit_msg.hideturtle()
exit_msg.penup()
exit_msg.goto(0, -300)
exit_msg.write("Type 'Exit' to exit the game.", font=('Arial', 16, 'normal'))





# Convert the csv of the states names into a dataframe
import pandas as pd
data = pd.read_csv('./50_states.csv')
print(data)

all_state_list = data.state.to_list()
print(all_state_list)
states_guessed_correctly = []


# Create a while loop so to repeatedly ask user for the guess until all the states have been guessed or he answered wrong

while len(states_guessed_correctly) < len(data):
    user_guess = screen.textinput(f"{len(states_guessed_correctly)} / {len(data)} of the states Guessed", "Guess the name of the State in US")
    user_guess = user_guess.title()
    # for i in range(len(data)):
    if user_guess == 'Exit':
        #create a csv file for the list of the states not answered
        # remaining_states = []
        # for state_name in all_state_list:
        #     if state_name not in states_guessed_correctly:
        #         remaining_states.append(state_name)

        #using list comprehension method
        remaining_states =[state for state in all_state_list if state not in states_guessed_correctly]

        #create csv from the list
        pandas.DataFrame(remaining_states).to_csv("./remaining_states.csv")
        break

    elif user_guess in states_guessed_correctly:
        pass

    elif user_guess in all_state_list:
        states_guessed_correctly.append(user_guess)

        #print state name at the correct location
        t = Turtle()
        t.hideturtle()
        t.penup()
        correct_state_row = data[data.state == user_guess]
        x_cord = int(correct_state_row.x)
        y_cord = int(correct_state_row.y)
        t.goto((x_cord, y_cord))
        t.write(f"{user_guess}")
        # print(states_guessed_correctly)



# screen.mainloop()



    #     details = (i , data.x[i] , data.y[i])
    # # print(data.state)






# # Do something to get the coordinates of the points where mouse is clicked.
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# Managing screen to not exit when clicked on screen
# screen.mainloop()  # this is an alternative to exitonclick function --> this does not exitonclick -> and we need this as we have to click on the screen to know its coordinates
# screen.exitonclick()
