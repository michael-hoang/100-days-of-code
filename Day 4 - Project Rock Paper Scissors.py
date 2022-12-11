rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >=3 or choice <0:
  print("Please only enter 0 for Rock, 1 for Paper or 2 for Scissors.")
elif choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)

cpu_choice = random.randint(0, 2)
if choice >=3 or choice <0:
  print()
else:
  print("Computer chose:")
  if cpu_choice == 0:
    print(rock)
  elif cpu_choice == 1:
    print(paper)
  else:
    print(scissors)

win = [choice == 0 and cpu_choice == 2, choice == 1 and cpu_choice == 0, choice == 2 and cpu_choice == 1]
lose = [choice == 0 and cpu_choice == 1, choice == 1 and cpu_choice == 2, choice == 2 and cpu_choice == 0]

if choice >=3 or choice <0:
  print()
else:
  if win[0] or win[1] or win[2]:
    print("You win!")
  elif lose[0] or lose[1] or lose[2]:
    print("You lose!")
  else:
    print("It's a draw!")



