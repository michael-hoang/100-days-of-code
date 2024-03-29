from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

import random

"""
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def get_dict(self) -> dict:
        """Return a Dictionary object containing data of cafe."""
        cafe_data = {}
        for col in self.__table__.columns:
            cafe_data[col.name] = getattr(self, col.name)
        sorted(cafe_data)
        return cafe_data


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalar()

    # # Alternatively...
    # result = db.session.execute(db.select(Cafe))
    # all_cafes_rows = result.scalars()
    # all_cafes_list = all_cafes_rows.all()
    # random_cafe = random.choice(all_cafes_list)

    sorted_keys = sorted(random_cafe.__dict__.keys())
    sorted_keys.remove("_sa_instance_state")
    cafe_data = {}
    for key in sorted_keys:
        cafe_data[key] = getattr(random_cafe, key)

    return jsonify(cafe=cafe_data)


@app.route("/all")
def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars()
    all_cafes_data = []
    for cafe in all_cafes:
        all_cafes_data.append(cafe.get_dict())

    return jsonify(cafes=all_cafes_data)


@app.route("/search")
def search():
    location = request.args.get("loc")
    query = db.select(Cafe).where(Cafe.location == location)
    rows = db.session.execute(query)
    # rows_as_list = rows.all()
    cafes = rows.scalars()
    cafes_as_list = cafes.all()
    if cafes_as_list:
        return jsonify(cafes=[cafe.get_dict() for cafe in cafes_as_list])

    else:
        return jsonify(
            error={"Not Found": "Sorry, we don't have a cafe at that location."}
        )


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(int(request.form.get("sockets"))),
        has_toilet=bool((int)),
        has_wifi=bool(int(request.form.get("wifi"))),
        can_take_calls=bool(int(request.form.get("calls"))),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.session.get(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(success="Successfully updated the price."), 200
    else:
        return jsonify(
            error={
                "Not Found": "Sorry a cafe with that id was not found in the database."
            }
        ), 404


## HTTP DELETE - Delete Record


if __name__ == "__main__":
    app.run(debug=True)
