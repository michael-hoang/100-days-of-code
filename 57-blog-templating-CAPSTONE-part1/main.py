import requests

from flask import Flask, render_template
from post import Post


app = Flask(__name__)
data = Post()


@app.route("/")
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    if response.status_code == 200:
        all_posts = response.json()
        data.all_posts = all_posts
    return render_template("index.html", posts=all_posts)


@app.route("/post/<int:id>")
def read_post(id):
    for post in data.all_posts:
        if post["id"] == id:
            title = post["title"]
            subtitle = post["subtitle"]
            body = post["body"]
    return render_template("post.html", title=title, subtitle=subtitle, body=body)


if __name__ == "__main__":
    app.run(debug=True)
