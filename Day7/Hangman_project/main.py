'''
there will be a word , and user have to guess all the characters of the word, in few attempts... for each coorect guess , his chances will not be reduced and the position of the correct letter guess correctly will be shown. 
for each wrong guess , his chances will be deducted.
after all the chances have been used , the game is over and player is lost.
but if all the letters have been correctly guessed , then he will be the winner.
'''
'''
my strategy..
first form the word in the form of list
'''
import random ;
from hangman_art import logo, stages
from hangman_words import word_list;
import os;

# Welcome message 
print(logo)

selected_word = word_list[random.randint(0,len(word_list))]
print(selected_word)
# selected_word_list = [] # no need
# for i in range(0,len(selected_word)):
#     selected_word_list.append(selected_word[i])



correct_guessed_till_now = []
for i in range(0,len(selected_word)):
    correct_guessed_till_now.append('_')

print(correct_guessed_till_now)

# checking if the guessed letter is correct
# def list_compare(list1,list2) :
#     result = True;
#     for i in range (0,len(list1)):
#         if list1[i] != list2[i]:
#             result = False;
#     return result;
    


remaining_chances = 7;
# while remaining_chances != 0 and  list_compare(selected_word , correct_guessed_till_now) == False:
while remaining_chances != 0 and  '_' in correct_guessed_till_now:
    
    guess_letter = input("guess a letter in the word \n")
    
    os.system('clear') # this will clear the terminal after every guess -- > imported from the os module.


    for i in range(0, len(selected_word)):
        if guess_letter == selected_word[i]:
            correct_guessed_till_now[i]= guess_letter;
            print("Guess is correct \n")
            print(f"{correct_guessed_till_now}\n" )
    

    if guess_letter not in selected_word:
        print("Wrong Guess ")
        print(stages[remaining_chances-1])
        remaining_chances -=1;
    
    print(f"Reamining chances : {remaining_chances}")
  
    

# if list_compare(selected_word , correct_guessed_till_now) == True:
#     print("Well Done You won !")
# else:
#     print("Sorry ! You failed to guess and chances to guess is over.")

if '_' not in correct_guessed_till_now:
    print("Well Done You won !")
else:
    print("Sorry ! You failed to guess and chances to guess is over.")
    print(logo)


