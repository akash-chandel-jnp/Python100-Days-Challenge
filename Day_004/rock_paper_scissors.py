rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
import random

choices = ["rock", "paper", "scissors"]
rand_num = random.randint(0, 2)
computer_choice = choices[rand_num]

myChoice = choices[
    int(input("enter a number , 0,1,2 for rock , paper , scissors respectively \n"))
]
print(
    f"You chose {myChoice.capitalize()} and computer chose {computer_choice.capitalize()}"
)
print(f"{myChoice} vs {computer_choice}")
if myChoice == "rock":
    if computer_choice == "paper":
        print("Computer Wins")
    elif myChoice == computer_choice:
        print("DRAW")
    else:
        print("You wins")
elif myChoice == "paper":
    if computer_choice == "scissors":
        print("Computer Wins")
    elif myChoice == computer_choice:
        print("DRAW")
    else:
        print("You wins")
else:
    if computer_choice == "rock":
        print("Computer wins")
    elif myChoice == computer_choice:
        print("DRAW")
    else:
        print("You wins")
