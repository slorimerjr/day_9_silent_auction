from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

#my solution
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

#teacher solution

bids = {} #1
bidding_finished = False #5

def find_highest_bidder(bidding_record): #10
    highest_bid = 0 #13
    winner = " " #16
    #{"Angela": 123, "James", 321}
    #Remeber: when using a for loop on a dictionary, instead of looping through each item in dic, it loops through each of the keys.
    for bidder in bidding_record: #11
        bid_amount = bidding_record[bidder] #12
        #bid_amount is where the value for each of the keys we call will be stored.
        #first loop will = 123, second will = 321.
        if bid_amount > highest_bid: #14
            highest_bid = bid_amount #15
            winner = bidder #17
    clear()
    print(f"The winner is {winner}, and they won with a bid of ${highest_bid}.") #18
        

while not bidding_finished: #6
    name = input("What is your name?: \n") #2
    price = int(input("What is your bid?:\n$")) #3 #20 added int
    bids[name] = price #4
    should_continue = input("Are there any other bidders? Type yes or no. \n") #7
    if should_continue == "no": #8
        bidding_finished = True #8
        find_highest_bidder(bids) #19
    elif should_continue == "yes":
        clear() #9

    