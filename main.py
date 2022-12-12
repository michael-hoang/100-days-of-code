import random
from tabnanny import check
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards(number=1):
    """Deal number of card(s) based on input and returns it. Default is 1."""
    dealt_cards = []
    for _ in range(number):
        dealt_cards.append(random.choice(cards))
    return dealt_cards

def calculate_score(hand : list):
    """Calculates and returns total score for cards in hand."""
    total_score = sum(hand)
    if total_score == 21 and len(hand) == 2:
        return 0 # 0 is Blackjack
    else:
        return total_score

def check_aces(hand):
    """Checks and converts value of Ace in hand from 11 to 1. Returns hand as list."""
    if 11 in hand:
        ace_position = hand.index(11)
        hand[ace_position] = 1
        return hand

def display_final_score(your_hand, your_score, cpu_hand, cpu_score):
    """Displays final hands and scores of all players."""
    print(f"\tYour final hand: {your_hand}, final score: {your_score}")
    print(f"\tComputer's final hand: {cpu_hand}, final score: {cpu_score}")


def play_blackjack():
    your_cards = deal_cards(2)
    cpu_cards = deal_cards(2)
    game_active = True

    print(logo)

    while game_active:
        your_score = calculate_score(your_cards)
        cpu_score = calculate_score(cpu_cards)
        print(f"\tYour cards: {your_cards}, current score: {your_score}")
        print(f"\tComputer's first card: {cpu_cards[0]}")

        if your_score == 0:
            display_final_score(your_cards, your_score, cpu_cards, cpu_score)
            print("You win with a Blackjack")
            game_active = False
        elif cpu_score == 0:
            display_final_score(your_cards, your_score, cpu_cards, cpu_score)
            print("Lose, opponent has Blackjack 😭")
            game_active = False
        elif your_score > 21:
            check_aces(your_cards)

        
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            your_cards.append(deal_cards())
            your_score = calculate_score(your_cards)
            if your_score > 21:
                your_cards = check_aces(your_cards)





want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if want_to_play == 'y':
    play_blackjack()