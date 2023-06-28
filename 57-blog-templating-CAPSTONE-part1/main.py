import requests

from flask import Flask, render_template
from post import Post


app = Flask(__name__)

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
if response.status_code == 200:
    post_obj = Post(response.json())


@app.route("/")
def home():
    return render_template("index.html", posts=post_obj.all_posts)


@app.route("/post/<int:id>")
def read_post(id):
    post = post_obj.all_posts[id]
    return render_template(
        "post.html", title=post["title"], subtitle=post["subtitle"], body=post["body"]
    )


if __name__ == "__main__":
    app.run(debug=True)
