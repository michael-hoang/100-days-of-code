from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, TimeField, URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


def get_emoji_ratings(emoji: str) -> list:
    """Return a list of the provided emoji as ratings on a scale from 1-5."""
    return [emoji * i for i in range(1, 6)]


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])

    # Exercise:
    # add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
    # make coffee/wifi/power a select element with choice of 0 to 5.
    # e.g. You could use emojis ☕️/💪/✘/🔌
    # make all fields required except submit
    # use a validator to check that the URL field has a URL entered.
    # ---------------------------------------------------------------------------
    location_url = URLField(
        "Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()]
    )
    open_time = TimeField("Open Time e.g. 8AM", validators=[DataRequired()])
    close_time = TimeField("Close Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=get_emoji_ratings("☕️"),
        validators=[DataRequired()],
    )
    wifi_str_rating = SelectField(
        "Wifi Strength Rating",
        choices=["✘"] + get_emoji_ratings("💪"),
        validators=[DataRequired()],
    )
    # ---------------------------------------------------------------------------
    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open("cafe-data.csv", newline="") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
