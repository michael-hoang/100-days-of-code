from art import logo, vs
from game_data import data
import random
import os
clear = lambda: os.system('cls')

data_copy = data[:]
# pick random index from 0-49 and assign to A.
rand_index = random.choice(range(len(data_copy)))
a = data_copy.pop(rand_index)
# pick random index from 0-48 and assign to B.
rand_index = random.choice(range(len(data_copy)))
b = data_copy.pop(rand_index)
# Reset data list back to original
data_copy = data[:]

score = 0
game_running = True

while game_running:
    clear()
    print(logo)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")    
    print(vs)
    print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
    more_follower = input("Who as more followers? Type 'A' or 'B': ").upper()
    if more_follower == "A":
        if a["follower_count"] > b["follower_count"]:
            score += 1
            print(logo)
            print(f"You're right! Current score: {score}.")
            # pop off A from the data_copy list to avoid duplicate comparison
            data_copy = data[:]
            a_index = data_copy.index(a)
            data_copy.pop(a_index)
            # assign B to A
            a = b
            print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
            print(vs)
            # pick random B from updated data_copy list after A was popped off
            rand_index = random.choice(range(len(data_copy)))
            b = data_copy.pop(rand_index)
            print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_running = False

    elif more_follower == "B":
        if b["follower_count"] > a["follower_count"]:
            score += 1
            print(logo)
            print(f"You're right! Current score: {score}.")
            # pop off B from the data_copy list to avoid duplicate comparison
            data_copy = data[:]
            b_index = data_copy.index(b)
            data_copy.pop(b_index)
            # assign B to A
            a = b
            print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
            print(vs)
            # pick random B from updated data_copy list after A was popped off
            rand_index = random.choice(range(len(data_copy)))
            b = data_copy.pop(rand_index)
            print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")     
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}") 
            game_running = False