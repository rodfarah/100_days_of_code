from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class IdentityChecker(FlaskForm):
    """Class that represents a login form"""
    email = EmailField("Your E-mail", validators=[DataRequired()])
    password = PasswordField("Type Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


