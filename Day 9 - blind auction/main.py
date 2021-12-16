from replit import clear
#HINT: You can call clear() to clear the output in the console.

# Welcome Screen
from art import logo
print(logo)
print("Welcome to the secret autction program.\n")

# Initialization
proceed = True
bids = {}

# Highest bidder function
def best_bid(bid_record):
    # bid_record = {
    #    "name1": x
    #    "name2": y
    #    "name3": z
    # }
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        amount = bid_record[bidder]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


# Collecting Bids
while proceed:
    name = input("What is your name?: ")
    amount = round(float(input("What is your bid?: $")), 2)
    new_bid = input("Are there any other bidders? (yes/no): ").lower()
    bids[name] = amount
    if new_bid == "yes" or new_bid == "y":
        clear()
    else:
        proceed = False
        clear()
        best_bid(bids)