
# from os import system
# system('clear')
# print("Welcome to the Game :")
# from game_art import logo
# print(logo)
print("Guess who has Higher Followers on Instagram : \n")

# from celebrity_data import celebrity_list
celebrity_list = {
    "Cristiano Ronaldo" : [607,'Footballer	Portugal'],
    "Lionel Messi" : [488, 'Footballer	Argentina'],
    "Selena Gomez" : [430,'Actress	United States'],
    "Kylie Jenner" : [350,'Reality TV Star, Businesswoman	United States'],
    "Dwayne" :[650,'Actor, Producer, Retired Wrestler	United States'],
    "Ariana Grande" : [800,'Singer, Actress	United States'],
    "Kim Kardashian" : [560,'Reality TV Star, Businesswoman	United State']
}

# Make a dictionary whcih stores 'names of celebrity ' and their 'followers count' Better do it in another file and import it here

#Choose two celebrity in random order from the list 


import random

def select_two_celeb():
    
    celeb_1 , celeb_1_desc = random.choice(list(celebrity_list.items()))
    celeb_2 , celeb_2_desc = random.choice(list(celebrity_list.items()))
    celeb_1_follower = celeb_1_desc[0]
    celeb_2_follower = celeb_2_desc[0]

    winner_celb = find_winner_celeb(celeb_1,celeb_2,celeb_1_follower,celeb_2_follower)
    return [celeb_1,celeb_1_desc,celeb_2,celeb_2_desc,celeb_1_follower,celeb_2_follower,winner_celb]


def play_game():
    score=0

    selection_data= select_two_celeb()
    cb1 =selection_data[0]
    cb1_dsc = selection_data[1]
    cb2 =selection_data[2]
    cb2_dsc = selection_data[3]
    cb1_flw =selection_data[4]
    clb2_flw =selection_data[5]
    winner =selection_data[6]

    guess = prompt_user(cb1,cb2,cb1_dsc,cb2_dsc)

    isGuessCorrect = compare_guess(guess,winner)
    if isGuessCorrect==True:
        score+=1
        print(f"You score is : {score}")
        print("This line is wrong")
    else :
        score=0



#first you decide the correct answer: 
def find_winner_celeb(celb1,celb2,celb1_folwr , celeb2_folwr ):
    
    if celb1_folwr > celeb2_folwr:
        winr_celb = celb1
    elif celb1_folwr < celeb2_folwr:
        winr_celb = celb2
    return winr_celb

#Prompt the user to choose among the two 
def prompt_user(celb1, celb2,celb1_desc , celb2_desc):
    print(f"Compare : Type 'A' for {celb1} ,{celb1_desc[1]} with ")
    from game_art import versus  
    print(versus)
    print(f"Compare : Type 'B' for {celb2} ,{celb2_desc[1]}")

    user_input = input("Type you answer here : ").lower()
    if user_input == 'a':
        user_guess = celb1
    elif user_input == 'b':
        user_guess = celb2
    
    return user_guess

#compare the guess with the actual winner_celb(answer):
def compare_guess(user_guess,winner_celb):
    if user_guess == winner_celb:
        print("You guessed Right\n")
        # bring next challenge
        play_game()
        return True


    else :
        print(f"Sorry You guessed wrong , correct answer is {winner_celb}\n")
        # ask does he want to play again
        choice = input(f"Want to play again | 'y' or 'n' : ")
        if choice == 'y':
            play_game()
        else:
            print("Good Bye!")





play_game()