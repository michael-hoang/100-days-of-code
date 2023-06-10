#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: This method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# My solution:
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    message = starting_letter.read()

with open("./Input/Names/invited_names.txt") as invited_names:
    names_as_string = invited_names.read()

# .split() method <-- not recommended. any names with a space in between will get split. (Ex. Uncle Iroh)
names_as_list = names_as_string.split()

# .replace() method
for name in names_as_list:
    personalized_message = message.replace("[name]", name.title())
    with open(f"./Output/ReadyToSend/to_{name}.txt", mode="w") as personalized_letter:
        personalized_letter.write(personalized_message)



# Angela's solution:
PLACEHOLDER = "[name]"

# .readlines() method
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# .strip() method will get rid of trailing \n from .readlines() method
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        # .replace() method
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)



# Better solution:
PLACEHOLDER = "[name]"

# .splitlines() method
with open("./Input/Names/invited_names.txt") as names_file:
    names_contents = names_file.read()
    names = names_contents.splitlines()

# .replace() method
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_to {name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)