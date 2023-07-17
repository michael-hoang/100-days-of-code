import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField


class LoginForm(FlaskForm):
    email = StringField("Email")
    pw = StringField("Password")


app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
