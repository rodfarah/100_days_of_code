# import sqlite3

# db = sqlite3.connect("book-collection.db")
# cursor = db.cursor()
# # cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL, author varchar(250), rating FLOAT NOT NULL)")
# # cursor.execute("INSERT INTO books VALUES(1, 'The power of now', 'Eckhart Tolle', '9.2')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250))
    rating = db.Column(db.Float, nullable=False)

# with app.app_context():
#     db.create_all()

def add_items(table, title: str, author: str, rating: int):
    book = table(title=title, author=author, rating=rating)
    db.session.add(book)
    db.session.commit()

def read_all_data(table):
    content = db.session.execute(db.select(table).order_by(table.id)).scalars()
    for item in content:
        print(item.title)

def update_title_by_title(table, title, new_title):
    to_be_updated = db.session.execute(db.select(table).where(table.title == title)).scalar()
    to_be_updated.title = new_title
    db.session.commit()

def delete_by_id(table, id):
    to_be_deleted = db.session.execute(db.select(table).where(table.id == id)).scalar()
    db.session.delete(to_be_deleted)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
