import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    pw = PasswordField("Password", validators=[DataRequired(), Length(8)])
    submit = SubmitField("Log In")


app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")
EMAIL = "admin@email.com"
PASSWORD = "12345678"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == EMAIL and login_form.pw.data == PASSWORD:
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template("login.html", form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
