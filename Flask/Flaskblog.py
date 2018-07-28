from flask import Flask, render_template
app = Flask(__name__)

post = [
    {
        'author':'Rakesh Kumar A',
        'title': 'Blog Post 1',
        'content': 'First Post comment',
        'date_posted': '27 July, 2018'
    },
    {
        'author': 'Surabhi Bramhadev',
        'title': 'Blog Post 2',
        'content': 'Second Post comment',
        'date_posted': '26 July, 2018'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=post)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)