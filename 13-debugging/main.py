############DEBUGGING#####################

# # Describe Problem: The problem is in the logic. The value 20 in the range function is 
# # exclusive in this example. Calling my_function() won't print or return any result. Need 
# # to change 20 to 21.
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# # Problem: randint(1, 6) produces 1-6, list index is from 0-5. Index 6 is out of range.
# # Fix by changing to randint(0, 5)
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# # Problem is a logical error. The operator doesn't include equal to.
# # year = 1994 won't return any result.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# # Problem: age variable returns a str instead of int.
# # Problem: print() is not indented.
# # Problem: Need f-string to use multiple value types.
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # <--- assignment vs equality operator. This evaluates to True or False.
# # print(f"(Debugging) Word per page is: {word_per_page}") #<--- this prints integer 0
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item) # Need to indent this line so that it's inside the for loop in order to append each new_item to b_list.
  print(b_list)

mutate([1,2,3,5,8,13])