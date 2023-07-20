from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///all-books.db"
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(length=250), nullable=False, unique=True)
    author = db.Column(db.VARCHAR(length=250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_rows = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = all_rows.scalars()
    return render_template(
        "index.html",
        all_books=all_books,
        # .scalar() returns None if no results come back from .select query
        contain_books=db.session.execute(db.select(Book)).scalar(),
    )


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        pass

    return render_template("edit.html")


if __name__ == "__main__":
    app.run(debug=True)
