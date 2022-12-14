import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.penup()

# Need to get a list of 50 states
states_df = pd.read_csv("50_states.csv")
state_column = states_df["state"]
states_list = state_column.tolist() # to_list() is just an alias for tolist()

# Neet to get coordinates of states as a list of tuples
x_column = states_df["x"]
y_column = states_df["y"]
coordinate_zip_object = zip(x_column, y_column) # creates zip object, an iterator of tuples. zip(iterator1, iterator2,...)
coordinates_list = list(coordinate_zip_object) # convert object to list.

# Combine both 50 states and coordinates lists into a dictionary.
states_coordinates_zip_object = zip(states_list, coordinates_list)
states_coordinates_list = list(states_coordinates_zip_object)
states_coordinates_dict = dict(states_coordinates_list)

# Main game
correct_guesses = []
score = 0

answer_state = screen.textinput(title="Guess the State", prompt="What's another states's name?").title()

while states_list:
    if answer_state == "Exit":
        break

    if answer_state in states_list:
        index = states_list.index(answer_state)
        correct_guess = states_list.pop(index)
        correct_guesses.append(correct_guess)
        score += 1
        my_turtle.goto(states_coordinates_dict[answer_state])
        my_turtle.write(answer_state)

    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another states's name?").title()

# Export states_to_learn.csv
if states_list:
    states_not_guessed = states_list # because we used the .pop() method in the Main game program
    states_not_guessed_df = pd.DataFrame(states_not_guessed)
    states_not_guessed_df.to_csv("states_to_learn.csv", header=False, index=False)


# def get_mouse_click_coor(x, y):
#     """Prints coordinate at mouse click location."""
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor) # onscreenclick listener - listens for mouse click

# turtle.mainloop() # alternative to screen.exitonclick()
# screen.exitonclick()