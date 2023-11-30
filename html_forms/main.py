from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")
        print(name, password)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
