import datetime as dt
import requests

from flask import Flask, render_template

SAMPLE_BLOG_API = "https://api.npoint.io/8f8112d0970cce098676"

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get(SAMPLE_BLOG_API)
    if response.status_code == 200:
        blogs = response.json()
    curr_date = dt.datetime.now().strftime("%B %d, %Y")

    return render_template(
        "index.html",
        blogs=blogs,
        date=curr_date
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
