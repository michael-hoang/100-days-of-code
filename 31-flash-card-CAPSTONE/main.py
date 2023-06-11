from tkinter import *
from typing import final
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Ariel", 40, "italic")
FONT_2 = ("Ariel", 60, "bold")


# def next_card():
#     # Select random word
#     next_word = random.choice(formatted_word_list).keys()
#     next_word_string = "".join(next_word)
#     canvas.itemconfig(language, text="Spanish")
#     canvas.itemconfig(word, text=next_word_string)

# def count_down(count):
#     if  count > 0:
#         root.after(1000, count_down, count-1)
#     else:
#         flip_card()

def next_card():
    global next_word, timer
    root.after_cancel(timer) # Cancels previous timer
    next_word = random.choice(word_list)
    spanish_word = next_word["Spanish"]
    canvas.itemconfig(language, text="Spanish", fill="black")
    canvas.itemconfig(word, text=spanish_word, fill="black")
    canvas.itemconfig(card, image=card_front_img)
    # Timer
    timer = root.after(ms=3000, func=flip_card) # <-- can also pass next_word as parameter to func=flip_card to avoid using global.
    words_to_learn()

def flip_card():
    english_word = next_word["English"]
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")

def remove_card():
    word_list.remove(next_word)
    next_card()

def words_to_learn():
    words_to_learn_df = pd.DataFrame(word_list)
    words_to_learn_df.to_csv("data/words_to_learn.csv", index=False)


try:
    file = "data/words_to_learn.csv"
    df = pd.read_csv(file)
except FileNotFoundError:
    # Create DataFrame --> List of dictionaries
    file = "data/spanish_words.csv"
    df = pd.read_csv(file)
finally:
    word_list = df.to_dict(orient="records") # Creates list of dictionaries.
    # formatted_word_list = [{pair["Spanish"]: pair["English"]} for pair in word_list]

# Create GUI
root = Tk()
root.title("Flashy")
root.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
# Timer
timer = root.after(ms=3000, func=flip_card) # func gets called after timer expires.

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
language = canvas.create_text(400, 150, text="Language", font=FONT_1)
word = canvas.create_text(400, 263, text="Word", font=FONT_2)
canvas.grid(column=0, row=0, columnspan=2)

# card_front_img = PhotoImage(file="images/card_front.png")
# card_front_label = Label(image=card_front_img, bg=BACKGROUND_COLOR)
# card_front_label.grid(column=0, row=0, columnspan=2)

# language = Label(text="Language", font=FONT_1, bg="white")
# language.place(x=400, y=150, anchor=CENTER)

# word = Label(text="Word", font=FONT_2, bg="white")
# word.place(x=400, y=263, anchor=CENTER)

skip_button_img = PhotoImage(file="images/wrong.png")
skip_button = Button(image=skip_button_img, highlightthickness=0, borderwidth=0, \
    activebackground=BACKGROUND_COLOR, command=next_card)
skip_button.grid(column=0, row=1)

correct_button_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_button_img, highlightthickness=0, borderwidth=0, \
    activebackground=BACKGROUND_COLOR, command=remove_card)
correct_button.grid(column=1, row=1)


# Call this function before mainloop to display random word when starting the app.
next_card()

root.mainloop()