#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from time import sleep
import random
import os
clear = lambda: os.system('cls')

# Generate a random number from 1 to 100
list_100 = list(range(1, 101))
secret_num = random.choice(list_100)

# Game start
def game_start():
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {secret_num}")
    return input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Checks if guessed number is higher or lower than secret number
def check_number(guessed_number, secret_number):
    if guessed_number > secret_number:
        return "Too high."
    elif guessed_number < secret_number:
        return "Too low."
    else:
        return f"You got it! The answer was {secret_number}."

# Guess number loop
def guess_number():
    def guess_number_recursion():
        global attempts
        while attempts > 0:
            print(f"You have {attempts} remaining to guess the number.")
            guess = int(input("Make a guess: "))
            result = check_number(guess, secret_num)
            print(result)
            if result == f"You got it! The answer was {secret_num}.":
                attempts = 0
            else:
                result != f"You got it! The answer was {secret_num}."
                attempts -=1
                if attempts == 0:
                    print("You've run out of guesses, you lose.")
                else:
                    guess_number_recursion()
           
    guess_number_recursion()
    return False

level = game_start()
game_running = True

while game_running:
    if level == "easy":
        attempts = 10
        game_running = guess_number()

    elif level == "hard":
        attempts = 5
        game_running = guess_number()
    else:
        clear()
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        print(f"Pssst, the correct answer is {secret_num}")
        print("Please type only 'easy' or 'hard'!")
        sleep(2)
        level = game_start()
        