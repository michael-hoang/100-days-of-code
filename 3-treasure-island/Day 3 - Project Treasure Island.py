print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

path_1 = (input('\nOn your right is a tropical forest, and on your left is a dark cave. Which way do you want to go \nType "right" or "left": ')).lower()

if not path_1 == "left":
  print("\nYou got eaten by a man-eating plant.\nGame Over!")
else:
  path_2 = input('\nYou find a torch and explore the dark cave. In front of you is a cave spring. What do you do? \nType "swim" or "wait": ').lower()
  if not path_2 == "wait":
    print("\nYou got attacked by a water troll.\nGame Over!")
  else:
    path_3 = input('\nYou wait for 5 minutes and see 3 doors appear in front of you: a red door, a blue door, and a yellow door. Which color door do you want to open?\nType "red", "blue", or "yellow": ').lower()
    if path_3 == "red":
      print("\nThe Red Eyes Black Dragon flies out of the red door and attacks you with Inferno Fire Blast!\nGame Over!")
    elif path_3 == "blue":
      print("\nThe Blue Eyes White Dragon flies out of the blue door and attacks you with White Lightning!\nGame Over!")
    elif path_3 == "yellow":
      print("\nPIKA-BOO! Pikachu jumps out of the yellow door and does the Pika-dance. \nYou win!")
    else:
      print("\nGame Over!")

