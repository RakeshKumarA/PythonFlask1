from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Hello World to you all!</h1>"

@app.route("/about")
def about():
    return "<h1>About page</h1>"


if __name__ == '__main__':
    app.run(debug=True)