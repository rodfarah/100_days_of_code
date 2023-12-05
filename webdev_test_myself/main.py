from flask import Flask, render_template, redirect, url_for
from decouple import config
from form import IdentityChecker
SECRET_KEY = config("CSRF_TOKEN")


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def home_func():
    return render_template('index.html')

@app.route('/test', methods=['GET', 'POST'])
def test_func():
    email = None
    password = None
    test_form = IdentityChecker()

    if test_form.validate_on_submit():
        email = test_form.email.data
        test_form.email.data = ''
        password = test_form.password.data
        test_form.password.data = ''
        if email == "rodrigo@email.com" and password == "1234":
            return redirect(url_for('checked_in_func'))
        else:
            return redirect(url_for('denied_func'))
    
    return render_template('test.html', email=email, password=password, form=test_form)

@app.route('/denied')
def denied_func():
    return render_template('denied.html')

@app.route('/checked-in')
def checked_in_func():
    return render_template('checked-in.html')

@app.route('/goodbye')
def goodbye_func():
    return render_template('goodbye.html')




if __name__ == "__main__":
    app.run(debug=True)