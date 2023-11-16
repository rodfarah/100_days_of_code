from flask import Flask, render_template
from datetime import datetime
import requests as rq

GENDER_ENDPOINT = "https://api.genderize.io"
AGE_ENDPOINT = "https://api.agify.io"


app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/guess/<input_name>")
def home(input_name):
    params = {
        "name": input_name
    }

    gender_ticket = rq.get(url=GENDER_ENDPOINT, params=params)
    age_ticket = rq.get(url=AGE_ENDPOINT, params=params)
    just_gender = gender_ticket.json()["gender"]
    just_age = age_ticket.json()["age"]

    year = datetime.now().year
    return render_template("guess.html", year=year, name=input_name, gender=just_gender, age=just_age)


if __name__ == "__main__":
    app.run(debug=True)
