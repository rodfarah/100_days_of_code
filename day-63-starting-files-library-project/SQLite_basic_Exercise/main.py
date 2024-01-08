from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50))
    rating = db.Column(db.Float, nullable=False)


if not os.path.exists('book-collection.db'):
    with app.app_context():
        db.create_all()


def db_query(id):
    target_book = db.session.execute(
        db.select(Book).where(Book.id == id)).scalar_one_or_none()
    return target_book


@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.id)).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template('add.html')


@app.route('/delete', methods=["POST"])
def delete():
    to_be_deleted = db_query(request.form['id'])
    db.session.delete(to_be_deleted)
    db.session.commit()
    return home()


@app.route('/edit', methods=["POST", "GET"])
def edit():
    title = request.form['title']
    old_rating = request.form['rating']
    id = request.form['id']
    return render_template('edit.html', id=id, title=title, old_rating=old_rating)


@app.route('/edit-process', methods=['POST', 'GET'])
def process():
    almost_edited = db_query(request.form['id'])
    almost_edited.rating = request.form['new_rating']
    db.session.commit()
    return home()


if __name__ == "__main__":
    app.run(debug=True)
