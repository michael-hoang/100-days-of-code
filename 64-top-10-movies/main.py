from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-ratings.db"
Bootstrap5(app)

db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    """An ORM-based model of an SQL table called 'movies'."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(length=250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.VARCHAR(length=1000))
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.VARCHAR(length=1000))
    img_url = db.Column(db.VARCHAR(length=2048))


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
