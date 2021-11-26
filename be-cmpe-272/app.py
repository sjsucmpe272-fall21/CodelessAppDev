from flask import Flask
from flask_github import GitHub

app = Flask(__name__)
app.config['GITHUB_CLIENT_ID'] = '3aab68cf0f350df369ce'
app.config['GITHUB_CLIENT_SECRET'] = '3c438f4b1420c901ca89cc73a233e5865d9f8d2f'

github = GitHub(app)


@app.route('/login')
def login():
    return github.authorize()


@app.route('/hello')
def hello_world():
    return "hello world"


@app.route('/landingpage')
def landing_page():
    return "Landing Page"


@app.route('/')
def home():
    return "Hello World!!!!!!!"


if __name__ == '__main__':
    app.run()
