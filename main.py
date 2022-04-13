from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)



def silent_auction(user_name, user_bid, user_cont):
    auction = {}
    auction["name"] = user_name
    auction["bid"] = user_bid
    auction["user_cont"] = user_cont
        
      

cont_auction = "yes"

while cont_auction == "yes":
    print("Welcome to the secret auction program.")
    name = input("What is your name?\n")
    bid = input("What's your bid?\n$")
    cont = input("Are there any other bidders? yes/no\n").lower()
    cont_auction = cont
    clear()
    
    silent_auction(user_name=name, user_bid=bid, user_cont=cont)
