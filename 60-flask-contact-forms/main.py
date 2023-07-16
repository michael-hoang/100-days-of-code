import email.message
import os
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
        # Format message using email.message
        message = email.message.Message()
        message["Subject"] = f"Mike's Blog - Message from {data['name']}"
        msg_body = (
            data["message"]
            + f"\n\nEmail: {data['email']}\nPhone number: {data['phone']}"
        )
        message.set_payload(msg_body)
        # Load environment variables and send email
        load_dotenv()
        my_email = os.getenv("email")
        send_gmail(
            user_email=my_email,
            user_pw=os.getenv("password"),
            message=message.as_string(),
        )

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
