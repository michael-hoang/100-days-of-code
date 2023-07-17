import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    pw = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
