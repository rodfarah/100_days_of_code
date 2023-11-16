from flask import Flask, render_template
import requests as rq
from post import Post

API_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"


response = rq.get(url=API_ENDPOINT)

all_posts = response.json()
post_obj_list = []
for post in all_posts:
    post_object = Post(post["id"], post["title"],
                       post["subtitle"], post["body"])
    post_obj_list.append(post_object)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", pl=post_obj_list)


@app.route("/post/<int:num>")
def each_post(num: int):
    return render_template(
        "post.html", number=num,
        post_title=all_posts[num - 1]["title"],
        post_body=all_posts[num - 1]["body"]
    )


if __name__ == "__main__":
    app.run(debug=True)
