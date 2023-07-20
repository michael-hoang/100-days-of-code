from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Create database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# Create the extension
db = SQLAlchemy()
# Initialize the app with the extension
db.init_app(app)


# Create table model
class Book(db.Model):
    """An ORM model representing a 'books' SQL table."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.VARCHAR(length=250), nullable=False, unique=True)
    author = db.Column(db.VARCHAR(length=250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f"<Book {self.title}>"


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# Create record
with app.app_context():
    book1 = Book(title="Harry Potter", author="J.K. Rowling", rating=9.3)
    book2 = Book(
        title="Harry Potter and the Sorcerer's Stone", author="J.K. Rowling", rating=9.3
    )
    book3 = Book(
        title="Harry Potter and the Chamber of Secrets",
        author="J.K. Rowling",
        rating=9.3,
    )
    book4 = Book(
        title="Harry Potter and the Prisoner of Azkaban",
        author="J.K. Rowling",
        rating=9.3,
    )
db.session.add(book1)
# db.session.add_all([book1, book2, book3])
db.session.add(book4)
db.session.commit()

# Read all records
with app.app_context():
    rows_result_obj = db.session.execute(db.select(Book))
    all_books = rows_result_obj.scalars()
    for book in all_books:
        print(book.title)

    rows_result_obj_sorted = db.session.execute(db.select(Book).order_by(Book.title))
    all_books_sorted = rows_result_obj_sorted.scalars()
    for book in all_books_sorted:
        print(book.title)

# Read a particular record by query
with app.app_context():
    row_result_obj = db.session.execute(
        db.select(Book).where(Book.title == "Harry Potter")
    )
    book = row_result_obj.scalar()
    print(book.title)

# Update a particular record by query
with app.app_context():
    row_result_obj = db.session.execute(
        db.select(Book).where(Book.title == "Harry Potter")
    )
    book = row_result_obj.scalar()
    book.title = "New Harry Potter"
    db.session.commit()

# Update a record by Primary Key
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# Delete a particular record by Primary Key
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(
        db.select(Book).where(Book.id == book_id)
    ).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
