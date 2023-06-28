import requests

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    if response.status_code == 200:
        all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:blog_id>")
def read_post():
    return render_template("post.html")


if __name__ == "__main__":
    app.run(debug=True)
