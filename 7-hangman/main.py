import random
from hangman_words import word_list
from hangman_art import logo, stages

import os
clear = lambda: os.system('cls')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)
# print(f'Pssst, the solution is {chosen_word}.')

# Create blank chosen_word
display = []
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)}")
print(stages[lives])

guess_list = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    print(logo)
    # Keep track of guessed letters in guess_list
    if guess not in guess_list:
      guess_list.append(guess)
      # Replace blank with correct guessed letter  
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess: 
              display[position] = letter
      if guess in chosen_word:
          print(guess, "is in the word!")   
      # Subtract lives if letter guessed wrong.
      if guess not in chosen_word:
          print(guess, "is not in the word.")
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("YOU LOSE!")
      
      print(f"{' '.join(display)}")
  
      if "_" not in display:
          end_of_game = True
          print("YOU WIN!")

      print(stages[lives])

    else:
      print(guess, "is already guessed.")
      print(f"{' '.join(display)}")  
      print(stages[lives])
      