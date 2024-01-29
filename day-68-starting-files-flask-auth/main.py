from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# Create Database
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)



# Enable Flask Login
login_manager = LoginManager()
login_manager.init_app(app)


# Defining user_loader callback (https://flask-login.readthedocs.io/en/latest/#how-it-works)
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

# Create table in db
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        informed_email = request.form.get("email")
        informed_password = request.form.get("password")
        user_in_db = db.session.execute(db.select(User).where(User.email == informed_email)).scalar()
        # Check if user is already registered
        if user_in_db:
            flash("Email is already registered. Please, login.")
            return redirect(url_for("login"))
        # if user is realy a new user
        secured_password = generate_password_hash(
            password=informed_password,
            method="pbkdf2:sha256",
            salt_length=8
        )
        new_user = User(
            email=informed_email,
            password=secured_password,
            name = request.form.get("name")
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in=current_user.is_authenticated)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        users_email = request.form.get("email")
        password_informed = request.form.get("password")
        queried_user = db.session.execute(db.select(User).where(User.email == users_email)).scalar()
        
        # Validate Email and Password
        if not queried_user:
            flash("Email not found!")
            return redirect(url_for("login"))
        elif not check_password_hash(queried_user.password, password_informed):
            flash("Incorrect Password!")
            return redirect(url_for("login"))
        else:
            login_user(queried_user)
            return redirect(url_for("secrets"))
    return render_template("login.html", logged_in=current_user.is_authenticated)
        

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/download')
@login_required
def download_file():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
