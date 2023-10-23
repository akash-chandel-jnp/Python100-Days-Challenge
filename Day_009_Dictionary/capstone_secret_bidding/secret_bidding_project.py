import os
from logo_art import logo
print(logo)


def place_bid():
    

    name_and_bids = {}
    should_continue=True
    while should_continue == True:

        bidder_name =input("enter your name\n")
        bid_amount = int(input("Place you bid \n"))

        name_and_bids[bidder_name] = bid_amount

        os.system("clear")

        want_to_continue_or_not = input("to place more bid type 'Y' and to exit type 'N'")
        
        if want_to_continue_or_not =='N':
            should_continue = False

        print(name_and_bids)

    max_bid = 0;
    for name in name_and_bids:
        current_bid = name_and_bids[name]
        if current_bid > max_bid:
            max_bid = current_bid
            max_bidder = name
    print(f"The max bid is place by {max_bidder} of Rs.{max_bid}")

place_bid()
