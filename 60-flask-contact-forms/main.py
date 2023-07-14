import requests

from flask import Flask, render_template, request

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


@app.route("/post/<int:id>")
def post(id):
    for blog in blogs:
        if blog["id"] == id:
            return render_template("post.html", blog=blog)


@app.route("/form-entry", methods=["POST"])
def receive_data():
    data = request.form
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message.</h1>"


if __name__ == "__main__":
    app.run(debug=True)
