# Silent Auction by Robert Laurie
import art
print(art.logo)
print("Welcome to the Blind Auction Project")
bids = {}
loop = 0
while loop != -1:
    name = input("What is the bidders name?\n")
    bid = int(input(f"What is {name}\'s bid?\n$"))
    bids[name] = bid
    print(bids)
    loop = input("Are there more bids? Yes or No\n").lower().find("y")
max_bid = 0
winner = ""
for key in bids:
    bid = bids[key]
    print(bid)
    if bid > max_bid:
        max_bid = bid
        winner = key
print(f"The winner is {winner} with a bid of ${max_bid}")
