from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from decouple import config
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
CSRF_TOKEN = config("CSRF_TOKEN")

app = Flask(__name__)

# Create a 'secret key' (CSRF token)
app.config['SECRET_KEY'] = CSRF_TOKEN

# Create a form class


class LoginForm(FlaskForm):
    email = EmailField(label="Email", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    submit = SubmitField("Login")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    email = None
    password = None
    form = LoginForm()
    # Validade form
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = ""
        password = form.password.data
        form.password.data = ""
        # redirect form
        if email == "admin@email.com" and password == "12345678":
            return redirect(url_for('success'))
        else:
            return redirect(url_for('denied'))
    return render_template('login.html', email=email, password=password, form=form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/denied')
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
