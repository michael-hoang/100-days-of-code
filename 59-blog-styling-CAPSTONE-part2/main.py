import requests

from flask import Flask, render_template

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


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<title>")
def post(title):
    for blog in blogs:
        if blog["title"] == title:
            return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
