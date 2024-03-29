from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from helpers import (
    get_movie_description,
    get_poster_base_url_and_sizes,
    is_filled,
    search_movie,
)
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Optional


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-ratings.db"
db = SQLAlchemy()
db.init_app(app)

POSTER_BASE_URL, poster_sizes = get_poster_base_url_and_sizes()
# print(f"Poster base URL: {POSTER_BASE_URL}\nList of poster sizes: {poster_sizes}")
POSTER_SIZE_SM = poster_sizes[1]  # w154
POSTER_SIZE_LG = poster_sizes[4]  # w500


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


class AddMovieForm(FlaskForm):
    """Models a form to add new movies to favorites."""

    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Search Movie")


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
            # Update movie rankings in db
            all_movies = db.session.execute(
                db.select(Movie).order_by(Movie.rating.desc())
            ).scalars()
            ranking = 1
            for each_movie in all_movies:
                each_movie.ranking = ranking
                ranking += 1

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


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddMovieForm()
    if add_form.validate_on_submit():
        search_title = add_form.title.data
        movie_data = search_movie(movie=search_title)
        movie_results = movie_data["results"]
        num_results = movie_data["total_results"]
        total_pages = movie_data["total_pages"]
        return render_template(
            "select.html",
            movie_results=movie_results,
            num_results=num_results,
            poster_base_url=POSTER_BASE_URL,
            poster_size=POSTER_SIZE_SM,
            search_title=search_title,
            total_pages=total_pages,
        )

    return render_template("add.html", form=add_form)


@app.route("/select", methods=["GET", "POST"])
def select():
    movie_id = request.args["id"]
    new_movie = Movie(
        title=request.args["title"],
        year=request.args["release_year"],
        description=get_movie_description(movie_id),
        rating=None,
        ranking=None,
        review=None,
        img_url=POSTER_BASE_URL + POSTER_SIZE_LG + "/" + request.args["poster"],
    )
    db.session.add(new_movie)
    db.session.commit()
    # movie_ratings_id = (
    #     db.session.execute(
    #         db.select(Movie).filter(
    #             Movie.title.like(request.args["title"]),
    #             Movie.year.like(request.args["release_year"]),
    #         )
    #     )
    #     .scalar()
    #     .id
    # )
    return redirect(url_for("edit", movie_id=new_movie.id))


@app.route("/page")
def page():
    page_requested = int(request.args["page"])
    search_title = request.args["search_title"]
    movie_data = search_movie(movie=search_title, page=page_requested)
    movie_results = movie_data["results"]
    num_results = movie_data["total_results"]
    total_pages = movie_data["total_pages"]
    return render_template(
        "select.html",
        movie_results=movie_results,
        num_results=num_results,
        poster_base_url=POSTER_BASE_URL,
        poster_size=POSTER_SIZE_SM,
        search_title=search_title,
        total_pages=total_pages,
    )


if __name__ == "__main__":
    app.run(debug=True)
