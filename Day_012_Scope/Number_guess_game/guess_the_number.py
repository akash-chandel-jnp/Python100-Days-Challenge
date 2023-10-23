from art_logo import logo
import random

def set_difficulty():
    chances=0
    difficulty_level = input("type 'easy' for easy level and type 'hard' for hard level : ")
    if difficulty_level == 'easy':
        chances =10
    elif difficulty_level=='hard':
        chances = 5
    return chances

#write a function to compare the guess and the actual answer.
def compare_guess(num , turns): 
    '''Ask the user for a guess and compares with the actual answer and also tracks the chances remaining.'''
    while turns != 0:
        user_guess = int(input("Guess the number : "))
        if user_guess==num:
            print("You Won")
            turns=0
        else:
            if user_guess <num:
                print("You Guess is Smaller")
            elif user_guess > num:
                print("Your Guess is Larger")
            turns-=1
            print(f"chances left : {turns}")
            if turns==0:
                print("You lost")

#create function to check if he want to play again or not
def want_to_play_again():
    
    play_again =input("type 'y' to play again | type 'n' to exit : ")
    if play_again=='y':
        number_guessing_game()
    else:
        print("Godd Bye! ")


def number_guessing_game():
    print(logo) 
    print("Welcome to the Number Guessing Game ! \nI'm thinking of a number between 1 and 100 ")

    #computer choosed a random number
    the_number = random.randint(1,100)

    #choosing difficulty level
    chances_available = set_difficulty()
    
    print(f"You have {chances_available} chances.")

    #compare guess 
    compare_guess(the_number,chances_available)

    #ask whether wants to play again
    want_to_play_again()

 
    
number_guessing_game()
