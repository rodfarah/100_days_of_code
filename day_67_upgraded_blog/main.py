from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# RF CREATE FLASKFORM
class PostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Blog Post Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Background image url", validators=[DataRequired(), URL()])
    body = CKEditorField('Post content here', validators=[DataRequired()])
    submit = SubmitField('Submit')


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

@app.route('/post/<post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, ident=post_id)
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route("/new-post", methods=["GET", "POST"])
def add_new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        new_post = BlogPost(
            title = post_form.title.data,
            subtitle = post_form.subtitle.data,
            date = datetime.now().strftime("%B %d, %Y"),
            body = post_form.body.data,
            author = post_form.author.data,
            img_url = post_form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template('make-post.html', form=post_form)


@app.route("/edit-post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, ident=post_id)
    edit_form = PostForm(
        title = post.title,
        subtitle = post.subtitle,
        body = post.body,
        author = post.author,
        img_url = post.img_url
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.body = edit_form.body.data
        post.author = edit_form.author.data
        post.img_url = edit_form.img_url.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, to_be_edited = True)


# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>', methods=["GET", "POST"])
def delete_post(post_id):
    to_be_deleted = db.get_or_404(BlogPost, ident=post_id)
    db.session.delete(to_be_deleted)
    db.session.commit()
    return redirect(url_for("get_all_posts"))




# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
