import sqlite3

db = sqlite3.connect("book-collection.db")
cursor = db.cursor()
# cursor.execute("CREATE TABLE books(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL, author varchar(250), rating FLOAT NOT NULL)")
cursor.execute("INSERT INTO books VALUES(1, 'The power of now', 'Eckhart Tolle', '9.2')")
db.commit()