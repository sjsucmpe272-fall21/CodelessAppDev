# main.py

from flask import Flask, jsonify, redirect, render_template, url_for
from flask.ctx import RequestContext
from flask.globals import session
from flask_dance.contrib.github import github
from flask_dance.contrib.twitter import twitter
from flask_login import logout_user, login_required

from app.models import db, login_manager
from app.oauth import github_blueprint
from app.gpt3_api import get_flask_response
from flask import request


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./users.db"
app.secret_key = "supersecretkey"
app.register_blueprint(github_blueprint, url_prefix="/login")


db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/ping")
def ping():
    return jsonify(ping="pong")


@app.route("/")
def homepage():
    return render_template("index.html")


@app.route("/github")
def login_github():
    if not github.authorized:
        return redirect(url_for("github.login"))
    res = github.get("/user")
    session['id']=res.json()['id']
    username = res.json()["login"]
    print(session.get('id'))
    return f"You are @{username} on GitHub"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

@app.route("/flask_code_gen",methods =['GET', 'POST'])
def flask_code_generation():
    prompt="#create a flask route and method to verify if given number is prime"
    result=get_flask_response(prompt)
    if request.method=='POST':
        prompt = request.form['req_prompt']
        print(prompt)
        result = get_flask_response(prompt)
    return render_template("flask_code.html",prompt=prompt,result=result)


@app.route("/SQL_code_generation",methods =['GET', 'POST'])
def SQL_code_generation():

    prompt="#create a SQL query to get the number of users"
    result=get_flask_response(prompt)
    if request.method=='POST':
        prompt = request.form['req_prompt']
        print(prompt)
        result = get_flask_response(prompt)
    return render_template("SQL_code.html",prompt=prompt,result=result)
if __name__ == "__main__":
    app.run(debug=True)
