from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50))
    rating = db.Column(db.Float, nullable=False)

if not os.path.exists('book-collection.db'):
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    all_books = db.session.execute(db.select(Book).order_by(Book.id)).all()
    print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods = ["GET", "POST"])
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


if __name__ == "__main__":
    app.run(debug=True)

