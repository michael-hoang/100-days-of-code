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

num_let = 0
num_sym = 0
num_num = 0
password = ""
for letter in letters:
  if num_let < nr_letters:
    rand_let = random.choice(letters)
    password += rand_let
    num_let += 1
    
for symbol in symbols:  
  if num_sym < nr_symbols:
    rand_sym = random.choice(symbols)
    password += rand_sym
    num_sym += 1

for number in numbers:
  if num_num < nr_numbers:
    rand_num = random.choice(numbers)
    password +=rand_num
    num_num += 1

# Randomize generated password by putting each characters into a list and then random
total_nr_char = nr_letters + nr_symbols + nr_numbers
pass_list = []
rand_pass = ""
for character in password:
  pass_list.append(character)

# random.sample(list, k) will create a bug if length of sample (k) exceeds the number of unique characters in a list.
pass_list = random.sample(pass_list, total_nr_char)

for element in pass_list:
  rand_pass +=element

print(rand_pass)
