from art import logo, vs
from game_data import data
import random
import os 
clear = lambda: os.system('cls')

# Compare A vs B. 
print(logo)
## Randomly selects an index within range of data list and pop it off into varialbe a. 
rand_idx = random.choice(range(len(data)))
a = data.pop(rand_idx)
print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")

print(vs)
## Repeat same method for variable b.
rand_idx = random.choice(range(len(data)))
b = data.pop(rand_idx)
print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")


# Function. Ask who has more followers and compare follower_count to see which one is higher
score = 0
game_running = True
while game_running:
    more_follower = input("Who has more followers? Type 'A' or 'B': ").upper()
    if more_follower == "A":
        if  a["follower_count"] > b["follower_count"]:
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}")
            print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
            print(vs)
            rand_idx = random.choice(range(len(data)))
            b = data.pop(rand_idx)
            print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_running = False
    elif more_follower == "B":
        if  b["follower_count"] > a["follower_count"]:
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}")
            a = b
            print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
            print(vs)
            rand_idx = random.choice(range(len(data)))
            b = data.pop(rand_idx)
            print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_running = False
        




