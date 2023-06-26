import random

from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def display_h1_gif():
    gif = "<img src='./static/numbers.gif' alt='flashing-numbers-0-through-9'>"
    global secret_number
    secret_number = random.randint(0, 9)
    print(secret_number)
    return "<h1>Guess a number between 0 and 9</h1>" + gif


@app.route("/<number>")
def get_number(number):
    if not number.isdigit():
        return redirect("/")

    number = int(number)
    if number < secret_number:
        message = "Too low, try again!"
        image = "./static/low.gif"
        color = "red"
    elif number > secret_number:
        message = "Too high, try again!"
        image = "./static/high.gif"
        color = "purple"
    elif number == secret_number:
        message = "You found me!"
        image = "./static/correct.gif"
        color = "green"

    return f"<h1 style='color:{color};'>{message}</h1><img src='{image}' alt='puppy-img'>"


if __name__ == "__main__":
    app.run(debug=True)
