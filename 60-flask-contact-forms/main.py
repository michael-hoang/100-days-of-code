import requests

from dotenv import load_dotenv
from flask import Flask, render_template, request
from helpers import send_gmail

SAMPLE_BLOG_API = "https://api.npoint.io/8f8112d0970cce098676"
response = requests.get(SAMPLE_BLOG_API)
blogs = response.json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", blogs=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form

        return render_template(
            "contact.html", message="You've successfully sent your message."
        )

    return render_template("contact.html", message="Contact Me")


@app.route("/post/<int:id>")
def post(id):
    for blog in blogs:
        if blog["id"] == id:
            return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
