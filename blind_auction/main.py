from click import clear
from blind_auction_art import logo

def winner(dictionary: dict) -> list:
    """Return (highest bid, name)."""
    highest_bid = max([k for k in dictionary.keys()])
    return [highest_bid, dictionary[highest_bid]]

print(logo)
print("Welcome to the secret auction program.")

more_bidders = True
bidder_dict = dict()

while more_bidders:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bidder_dict.update({bid : name})
    others = input("Are there other bidders? Type 'yes' or 'no': ")

    if others == "no":
        who_wins = winner(bidder_dict)
        print(f"The winner is {who_wins[1]} with a bid of ${who_wins[0]}")
        more_bidders = False
    else:
        clear()

