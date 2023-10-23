from menu_and_ingredients import ingredients_list, money
from resources import *
from menu_and_ingredients import drink_available
from money_and_coins import coin_checker

# TODO 3: Print Report
""" a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml  
Coffee: 76g
Money: $2.5 """

# TODO 1: prompt user by asking "What would you like? (espresso/latte/cappuccino): ”
""" a. Check the user's input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer"""


def want_a_drink():
    isOn =True
    while isOn :
        user_choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()

        if user_choice=='off':
            isOn=False
        elif user_choice == 'repoklopok;loplrt':
            print_report()

        elif user_choice in drink_available:

            # call function check_resources_sufficiency() to check
            if check_resources_sufficiency(user_choice):
                # print("Resources checked and found sufficient ")

                # if user choose something then ask for money and check if he has enough money
                # better create function of checking money deposit and money return
                coin_checker(user_choice)

                # update the resources:
                update_resources(user_choice)

            else:
                print("Resources not available")

        else:
            print("You entered the wrong Drink name . plz correct it.")

        # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt.
        """a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
        the machine. Your code should end execution when this happens."""

       

        # def machine_on_off(on_off):
        #     global status
        #     status = on_off
        #
        #     # TODO 6: Check transaction successful?
        #     """
        #     a. Check that the user has inserted enough money to purchase the drink they selected.
        #     E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
        #     program should say “Sorry that's not enough money. Money refunded.”.
        #     b. But if the user has inserted enough money, then the cost of the drink gets added to the
        #     machine as the profit and this will be reflected the next time “report” is triggered. E.g.
        #     Water: 100ml
        #     Milk: 50ml
        #     Coffee: 76g
        #     Money: $2.5
        #     c. If the user has inserted too much money, the machine should offer change.
        #     E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
        #     places.
        #
        #     """
        #
        #     # TODO 7: Make Coffee.
        #     """
        #     a. If the transaction is successful and there are enough resources to make the drink the
        #     user selected, then the ingredients to make the drink should be deducted from the
        #     coffee machine resources.
        #     E.g. report before purchasing latte:
        #     Water: 300ml
        #     Milk: 200ml
        #     Coffee: 100g
        #     Money: $0
        #     Report after purchasing latte:
        #     Water: 100ml
        #     Milk: 50ml
        #     Coffee: 76g
        #     Money: $2.5
        #     b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
        #     latte was their choice of drink."""

        new_order = input("Want to order Something else: 'y' or 'n' : ")
        if new_order == 'y':
            want_a_drink()
        else:
            print("Have a good time! ")


want_a_drink()
