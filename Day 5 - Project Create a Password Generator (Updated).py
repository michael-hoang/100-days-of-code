#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Create password variable with no characters initially, and then concatenate letters, symbols, and numbers via 'for loop' based on user input of number of characters.
password = ""
for let in range(nr_letters):
  password += random.choice(letters)
for sym in range(nr_symbols):
  password += random.choice(symbols)
for num in range(nr_numbers):
  password += random.choice(numbers)

# Convert generated password string into a list via .append function.
password_list = []
for char in password:
  password_list.append(char)

# Shuffle the characters in the list via .shuffle function
random.shuffle(password_list)

# Reset password variable to have no characters and then concatenate each characters in the shuffled list back into a string
password = ""
for char in password_list:
  password += char
print(password)

