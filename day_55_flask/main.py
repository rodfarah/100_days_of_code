from flask import Flask

app = Flask(__name__)

def bold(func):
    def wrapper_func():
        return f'<b>{func()}</b>'
    return wrapper_func

@app.route("/")
@bold
def hello_word():
    return "hello, world!"


@app.route("/rod")
def hello_rod():
    return '<h1 style="text-align: center">hello, Rod!</h1> \
        <p>This is a Paragraph</p> \
        <img src="https://www.twoofus.com.br/wp-content/uploads/2019/06/RFarah_Fazenda-das-Cabras013.jpg" width="200px">'


@app.route("/<username>")
def user_greetings(username):
    return f"Hello, {username}"


if __name__ == "__main__":
    app.run(debug=True)
