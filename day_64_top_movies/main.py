from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, InputRequired, NumberRange
import requests
import os


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


@app.route("/")
def home():
    result = db.session.execute(
        db.select(Movie).order_by(desc(Movie.ranking)))
    all_movies = result.scalars()
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


if __name__ == '__main__':
    app.run(debug=True)
