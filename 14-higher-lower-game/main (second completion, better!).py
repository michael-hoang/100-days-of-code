from art import logo, vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')

def compare_followers(celeb1, celeb2):
    """Returns the celebrity with the highest follower count"""
    if celeb1["follower_count"] > celeb2["follower_count"]:
        return "A"
    else:
        return "B"

clear()
score = 0
game_running = True
A = random.choice(data)
print(logo)

while game_running: 
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    # print(f"Followers: {A['follower_count']}") 

    print(vs)
    B = random.choice(data)
    while B == A:
        B = random.choice(data)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    # print(f"Followers: {B['follower_count']}") 

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    more_follower = compare_followers(A, B)
    if choice == more_follower:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
        A = B
    else:
        game_running = False
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
