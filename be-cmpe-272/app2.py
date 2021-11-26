try:
    from flask import Flask, url_for, redirect, session
    from flask_dance.contrib.github import make_github_blueprint, github
    import os
    from dotenv import dotenv_values
except Exception as e:
    print("Some Modules are Missings {}".format(e))


app = Flask(__name__)

config = dotenv_values(".env") #get the values from here - config = {"USER": "foo", "EMAIL": "foo@example.org"}
app.config["SECRET_KEY"] = config["GITHUB_OAUTH_CLIENT_SECRET"]

github_blueprint = make_github_blueprint(client_id=config["GITHUB_OAUTH_CLIENT_ID"],
                                         client_secret=config["GITHUB_OAUTH_CLIENT_SECRET"])

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
    session.clear()
    return redirect('/')


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
