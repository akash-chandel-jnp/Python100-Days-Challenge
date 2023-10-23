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

my_choice = int(input("enter an number , 0 for rock | 1 for paper | 2 for scissors \n"))
computer_choice = random.randint(0, 2)
list = [rock, paper, scissors]

if my_choice >= 3 or my_choice < 0:
    print("You entered a wrong number")

else:  # continue the further processing
    print("My choice : ")
    print(list[my_choice])
    print("Computer choice : ")
    print(list[computer_choice])

    if my_choice == 0 and computer_choice == 3:
        print("You win")
    elif computer_choice == 0 and my_choice == 3:
        print("You Lost")
    elif my_choice > computer_choice:
        print("You won!")
    elif my_choice == computer_choice:
        print("It is a draw!")
