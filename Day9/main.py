import art

isProgramStop = False
bidders = {}

print(art.logo)
print("Welcome to the sectet auction program.")

while not isProgramStop:
    name = input("What is your name? ")
    bid = float(input("What's you bid: $"))

    bidders[name] = bid

    any_other_bidders = input("Are there any bidders? Type 'yes' or 'no'\n")
    if any_other_bidders.lower() == 'no':
        isProgramStop = True
    
winner_name = ""
highest_bid = 0

for bidderKey in bidders:
    if bidders[bidderKey] > highest_bid:
        highest_bid = bidders[bidderKey]
        winner_name = bidderKey
print(f"the winner is {winner_name} with a bid of ${highest_bid}")