from flask import Flask, render_template
import requests as rq

app = Flask(__name__)


@app.route("/")
def home():
    BLOG_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"
    ticket = rq.get(url=BLOG_ENDPOINT)
    all_posts = ticket.json()
    return render_template("index.html", ap=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
