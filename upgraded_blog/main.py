from flask import Flask, render_template

app = Flask("__main__")

@app.route('/')
def home():
    return render_template('index.html')

#TODO: @app.route('/about')
#def about():
#    return render_template('')

if __name__ == "__main__":
    app.run(debug=True)