from flask import Flask, render_template
import requests as rq

response = rq.get(url="https://api.npoint.io/79af83afe03463a29f67")
blog_content = response.json()


app = Flask("__main__")


@app.route('/')
def home():
    return render_template('index.html', ap=blog_content)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:num>')
def post(num):
    requested_post = None
    for post in blog_content:
        if post['id'] == num:
            requested_post = post
    return render_template('post.html', pst=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
