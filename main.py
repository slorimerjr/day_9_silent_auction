from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

all_bids = []

def silent_auction(user_name, user_bid):
    auction = {}
    auction["name"] = user_name
    auction["bid"] = int(user_bid)
    all_bids.append(auction)

def auction_winner():
    x = 0
    y = 0
    winner = " "
    for items in all_bids:
        if all_bids[x]["bid"] > y:
            y = all_bids[x]["bid"]
            winner = all_bids[x]["name"]
            x += 1
    clear()
    print(f"{winner} won the auction with a bid of ${y}.")

cont_auction = "yes"

while cont_auction == "yes":
    print("Welcome to the secret auction program.")
    name = input("What is your name?\n")
    bid = input("What's your bid?\n$")

    
    silent_auction(user_name=name, user_bid=bid)
    cont = input("Are there any other bidders? yes/no\n").lower()
    cont_auction = cont
    if cont_auction == "yes":
        clear()
    else:
        auction_winner()
    