try:
    from flask import Flask, render_template, url_for, request, redirect, make_response
    import random
    import json
    from time import time
    from random import random
    from flask_dance.contrib.github import make_github_blueprint, github
    from flask_login import logout_user
except Exception as e:
    print("Some Modules are Missings {}".format(e))


app = Flask(__name__)
app.config["SECRET_KEY"] = "3c438f4b1420c901ca89cc73a233e5865d9f8d2f"

github_blueprint = make_github_blueprint(client_id='3aab68cf0f350df369ce',
                                         client_secret='3c438f4b1420c901ca89cc73a233e5865d9f8d2f')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/login')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            # return '<h1>Your Github name is {}'.format(account_info_json['login'])
            return account_info_json
    return '<h1>Request failed!</h1>'


@app.route("/homepage")
def homepage():
    return "homepage"


@app.route("/logout")
def logout():
    logout_user()
    return redirect()


@app.route('/hello')
def hello_world():
    return "hello world from app2"


@app.route('/landingpage')
def landing_page():
    return "Landing Page"


@app.route('/')
def home():
    return "Hello World!!!!!!!"


if __name__ == "__main__":
    app.run(debug=True)
