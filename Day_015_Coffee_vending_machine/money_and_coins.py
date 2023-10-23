from resources import ingredients_list

# TODO 5: Process coins
"""a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.



b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52"""
money_balance = 0;


def coin_checker(drink_name):
    print("checking money")
    print("Please insert the coins")
    quarters_count = int(input("How many quarters : "))
    dimes_count = int(input("How many dimes : "))
    nickles_count = int(input("How many nickles : "))
    pennies_count = int(input("How many pennies : "))

    total_money = round((quarters_count * 0.25 + dimes_count * 0.10 + nickles_count * 0.05 + pennies_count * 0.01), 2)
    cost_of_drink = ingredients_list[drink_name]["cost"]
    print(f"cost of {drink_name} is ${cost_of_drink}")
    print(f"You deposited ${total_money}")

    # compare is money enough or not
    if total_money >= cost_of_drink:
        print(f"${round((total_money - cost_of_drink), 2)} is returned !")
        print(f"{drink_name} is getting ready")

        # update money_balance
        global money_balance;
        money_balance += cost_of_drink;
        print(f"Bal of money is : {money_balance}")


    elif total_money < cost_of_drink:
        print(f"Sorry that's not enough money. Money refunded.")
