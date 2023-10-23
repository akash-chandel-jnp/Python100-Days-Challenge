print("Welcome to the game of : ")
from art import logo , vs
print(logo)

import random
from game_data import data
c1=data[0]
print(c1)

c1_name =c1['name']
c1_folr =c1['follower_count']
c1_desc = c1['description']
c1_country = c1['country']

c2 =random.choice(data)
c2_name =c2['name']
print(c2)
c2_folr =c2['follower_count']
c2_desc = c2['description']
c2_country = c2['country']

# find the answer : who have greater followers
if c1_folr > c2_folr:
    winner = c1_name
else:
    winner = c2_name

#show the choices to the user
print(f"Compare : (a) {c1_name} , lives in  {c1_desc} {c1_country}")
#ask user his answer

input ("")





