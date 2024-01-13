from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired, NumberRange
import requests
from decouple import config
import os

TMDB_READ_ACCESS_TOKEN = config('TMDB_READ_ACCESS_TOKEN')
TMDB_BASIC_SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
TMDB_DETAILS_SEARCH_ENDPOINT = 'https://api.themoviedb.org/3/movie/'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Create db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define table


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(150), nullable=False)
    __table_args__ = (
        CheckConstraint('year >= 1900 AND year <= 2030',
                        name='check_year_digits'),
        CheckConstraint('rating >= 0 AND rating <= 10',
                        name='check max and min rating allowed'),
    )


# Create table if it does not exist yet
if not os.path.exists('top-movies.db'):
    with app.app_context():
        db.create_all()


# Define edit form
class EditForm(FlaskForm):
    float_validator = (InputRequired(), NumberRange(min=0, max=10))
    new_rating = FloatField('Your rating out of 10',
                            validators=float_validator)
    new_review = StringField('Your new review', validators=[DataRequired()])
    submit_button = SubmitField('Update')

# Define Add form


class AddForm(FlaskForm):
    title = StringField('Movie Title:', validators=[DataRequired()])
    submit_button = SubmitField('Add')

# Define TMDB API basic request


def tmdb_basic_request(title):

    params = {
        "query": title,
        "include_adult": "false",
        "language": "en-US",
        "page": "1"
    }

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_READ_ACCESS_TOKEN}",
    }
    response = requests.get(url=TMDB_BASIC_SEARCH_ENDPOINT,
                            params=params, headers=headers)
    response.raise_for_status()
    almost_there = response.json()
    results = almost_there["results"]
    return results

# Define TMDB API request for movie details by it's ID


def tmdb_details_request(id: int):
    params = {
        "language": "en-US"
    }
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_READ_ACCESS_TOKEN}",
    }
    response = requests.get(
        url=f"{TMDB_DETAILS_SEARCH_ENDPOINT}{id}", params=params, headers=headers)
    response.raise_for_status()
    result = response.json()
    return result


@app.route("/")
def home():
    result = db.session.execute(
        db.select(Movie).order_by(desc(Movie.rating)))
    all_movies = result.scalars().all()

    n = 1
    for movie in all_movies:
        movie.ranking = n
        n += 1
    db.session.commit()

    return render_template("index.html", all_movies=all_movies)

# Adding the update functionality


@app.route("/edit", methods=["GET", "POST"])
def edit_rating_review():
    form = EditForm()
    movie_id = request.args.get("id")
    to_be_updated = db.get_or_404(entity=Movie, ident=movie_id)

    if form.validate_on_submit():
        to_be_updated.rating = form.new_rating.data
        to_be_updated.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', form=form, to_be_updated=to_be_updated)


# Adding Delete functionality
@app.route('/delete')
def delete_movie():
    id_to_delete = request.args.get("id")
    to_be_deleted = db.get_or_404(entity=Movie, ident=id_to_delete)
    db.session.delete(to_be_deleted)
    db.session.commit()
    return redirect(url_for('home'))

# Adding Add functionality


@app.route('/add', methods=["POST", "GET"])
def add_movie():
    add_form = AddForm()
    if add_form.validate_on_submit():
        movie_title = add_form.title.data
        results = tmdb_basic_request(movie_title)
        return render_template("select.html", results=results)

    return render_template('add.html', form=add_form)

# Get TMDB details from a movie by its ID


@app.route('/details')
def fetch_details():
    movie_id = request.args.get("id")
    movie_details = tmdb_details_request(movie_id)
    new_movie = Movie(
        title=movie_details['title'],
        year=movie_details['release_date'][0:4],
        description=movie_details['overview'],
        img_url=f"https://image.tmdb.org/t/p/original{movie_details['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit_rating_review', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
