from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField, fields
from wtforms.validators import DataRequired, InputRequired, NumberRange, Optional
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-ratings.db"
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    """An ORM-based model of an SQL table called 'movies'."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(length=250), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.VARCHAR(length=1000), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.VARCHAR(length=1000), nullable=True)
    img_url = db.Column(db.VARCHAR(length=2048), nullable=False)


# with app.app_context():
#     db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg",
# )

# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg",
# )

# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()


class RateMovieForm(FlaskForm):
    """Models a movie rating form using FlaskForm."""

    rating = DecimalField(
        "Your Rating Out of 10 e.g. 7.5",
        render_kw={"step": "0.1"},
        validators=[NumberRange(min=0, max=10), Optional()],
    )
    review = StringField("Your Review")
    submit = SubmitField("Done")


def is_filled(field: fields) -> bool:
    """
    Return True if field is not empty.

    raw_data:
    If form data is processed, is the valuelist given from the formdata wrapper.
    Otherwise, raw_data will be None.
    """
    try:
        value = field.raw_data[0]
    except TypeError:
        return False
    else:
        if value == "":
            return False
    return True


@app.route("/")
def home():
    movies = db.session.execute(
        db.select(Movie).order_by(Movie.ranking.desc())
    ).scalars()

    return render_template("index.html", movies=movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    rating_form = RateMovieForm()
    if rating_form.validate_on_submit():
        if is_filled(rating_form.rating):
            movie.rating = rating_form.rating.data
        if is_filled(rating_form.review):
            movie.review = rating_form.review.data

        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=rating_form, movie=movie)


@app.route("/delete")
def delete():
    movie_id = request.args["movie_id"]
    movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
