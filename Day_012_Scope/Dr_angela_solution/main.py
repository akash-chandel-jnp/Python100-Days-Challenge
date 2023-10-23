from random import randint

# Function to check user's guess against aactual answer.
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else:
        print(f"You got it! The answer was {answer}")



# choosing a random number between 1 and 100 
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
answer = randint(1,100)

# make function to set difficulty


# Let the user guess a number 
guess = input("Guess a number ")

