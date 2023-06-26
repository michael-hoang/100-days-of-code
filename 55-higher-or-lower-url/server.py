from flask import Flask

app = Flask(__name__)


@app.route("/")
def display_h1_gif():
    gif = "<img src='./static/numbers.gif' alt='flashing-numbers-0-through-9'>"
    return "<h1>Guess a number between 0 and 9</h1>" + gif


if __name__ == "__main__":
    app.run(debug=True)
