from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField


class LoginForm(FlaskForm):
    email = StringField("email")
    pw = StringField("password")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
