from flask import Flask
from random import randint

random_number = randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:guess>")
def guess_number(guess):
    if random_number < guess:
        return '<h1 style="color: red">Too high! Try again.</h1>' \
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif random_number > guess:
        return '<h1 style="color: blue">Too low! Try again.</h1>' \
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color: green">Perfect! Wright answer!</h1>' \
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
