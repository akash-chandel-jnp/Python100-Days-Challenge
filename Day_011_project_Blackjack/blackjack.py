import random
import os
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 

dealer_cards = []
my_cards =[]

def add_card(list_name):
    random_idx =random.randint(0,12)
    # print(f"random index is {random_idx}")
    list_name.append( cards[random_idx])

def sum_of_cards(list):
    # sum=0
    # for card in list:
    #     sum+=card
    # print(f"sum of list is : {sum}")
    score = sum(list)
    return score
add_card(dealer_cards)


def play_blackjack():
    print(logo)

    print(f"dealer cards are : {dealer_cards} and sum is : {sum_of_cards(dealer_cards)}")

    add_card(my_cards)
    add_card(my_cards)
    print(f"my cards are : {my_cards} and sum is : {sum_of_cards(my_cards)}")

    should_continue = True
    while sum_of_cards(my_cards)<21  and should_continue == True:
        option_choosen =input(f"\nDo you want to 'hit' or 'stop': ")
        if option_choosen == 'hit':
            # call hit function
            add_card(my_cards)
            my_cards_sum = sum_of_cards(my_cards)

            os.system('clear')
            print(f"DEALER cards are : {dealer_cards} and SUM is : {sum_of_cards(dealer_cards)}")

            print(f"MY cards are : {my_cards} and SUM is : {my_cards_sum}")

            if my_cards_sum >21 :
                print("YOU LOSE - you went over 21.")
                should_continue=False


        else: # stop
            should_continue = False
            my_cards_sum = sum_of_cards(my_cards)
            
            dealer_sum = sum_of_cards(dealer_cards)
            while dealer_sum<17:
                add_card(dealer_cards)
                dealer_sum = sum_of_cards(dealer_cards)
                
            #call stop function
            # print(f"DEALER cards are : {dealer_cards} and SUM is : {sum_of_cards(dealer_cards)}")

            os.system('clear')
            print(f"DEALER cards are : {dealer_cards} and SUM is : {sum_of_cards(dealer_cards)}")

            print(f"MY cards are : {my_cards} and SUM is : {my_cards_sum}")

            if dealer_sum > 21:
                print("YOU WON -dealer went over 21.")
            elif  dealer_sum > my_cards_sum :
                print("YOU LOSE ")
            elif dealer_sum < my_cards_sum:
                print("YOU WON")
            elif dealer_sum == my_cards_sum:
                print("IT's A DRAW ")
            else:
                print("SOMETHING IS WRONG")

    play_again =input("\nDo you want to play again ! 'yes' or 'no' : ")
    if play_again== 'yes':
        #call whole game again
        print("game is starting again")
        play_blackjack()

    else:
        print("Good Bye")
                


play_blackjack()