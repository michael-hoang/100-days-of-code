import os
clear = lambda: os.system('cls')
from art import logo

def highest_bid(bid_log):
    highest_bid = 0
    highest_bidder = ""
    for name in bid_log:
        if bid_log[name] > highest_bid:
            highest_bid = bid_log[name]
            highest_bidder = name
    print(logo)
    print("Welcome to the secret auction program.")
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

auction_book = {}
auction_end = False

while not auction_end:
    print(logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    bid = int(input("What is your bid?: $"))
    auction_book[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bidders == "no":
        auction_end = True
    clear()

highest_bid(auction_book)