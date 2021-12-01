# main.py

from typing import final
from flask import Flask, jsonify, redirect, render_template, url_for
from flask.ctx import RequestContext
from flask.globals import current_app, session
from flask_dance.contrib.github import github
from flask_login import logout_user, login_required

from app.models import db, login_manager
from app.oauth import github_blueprint
from app.gpt3_api import get_flask_response,get_SQL_response
from flask import request
import base64
import requests
import json
import os
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./users.db"
app.secret_key = "supersecretkey"
app.register_blueprint(github_blueprint, url_prefix="/login")


db.init_app(app)
login_manager.init_app(app)

import base64
import requests
import json

def push_to_github(content,sha,user):
    filename="app.py"
    repo="suhasAB/Flask_Heroku_API"
    url="https://api.github.com/repos/"+repo+"/contents/"+filename
    content=content
    branch="main"
    token=os.getenv("COMMIT_TOKEN")
    data = requests.get(url, headers = {"Authorization": "token "+token}).json()
    print(data)
    sha=data["sha"]
    commitMsg="added new FlaskRoute by @"+user+" which was commited by @CodelessAppDev"
    
    message = json.dumps({"message": commitMsg,
                            "branch": branch,
                            "content": content,
                            "sha": sha
                            })

    resp=requests.put(url, data = message, headers = {"Content-Type": "application/json", "Authorization": "token "+token})
    return resp


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
    print(res.json())
    session['id']=res.json()['id']
    session['result']=res.json()['login']
    print(session['result'])
    username = res.json()["login"]
    print(session.get('id'))
    return "You are "+username+"on GitHub and details are\n"+str(res.json())

@app.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    return redirect(url_for("homepage"))

@app.route("/flask_code_gen",methods =['GET', 'POST'])
def flask_code_generation():
    prompt="#create a flask route and method to verify if an integer passed in url is prime"
    result=get_flask_response(prompt)
    session['result']=result
    if request.method=='POST':
        prompt = request.form['req_prompt']
        print(prompt)
        result = get_flask_response(prompt)
        session['result'] = result
    return render_template("flask_code.html",prompt=prompt,result=result)


@app.route("/SQL_code_generation",methods =['GET', 'POST'])
def SQL_code_generation():
    prompt="#create a SQL query to get the number of users in the database"
    result=get_SQL_response(prompt)
    session['result']=result
    get_SQL_response(prompt)
    if request.method=='POST':
        prompt = request.form['req_prompt']
        print(prompt)
        result=get_SQL_response(prompt)
        
    return render_template("SQL_code.html",prompt=prompt,result=result)

@app.route("/commit_code_to_create_api")
def commit_code_to_create_api():
    git_user=github.get("/user").json()['login']
    repo="suhasAB/Flask_Heroku_API"
    filename="app.py"
    repo_get_resp=requests.get("https://api.github.com/repos/"+repo+"/contents/"+filename).json()
    current_content_of_file=base64.b64decode(repo_get_resp['content']).decode('utf-8')
    sha=repo_get_resp['sha']
    new_content_of_file=(session['result'].encode('utf-8')).decode('utf-8')
    final_content_of_file=current_content_of_file+new_content_of_file
    encoded_final_code=base64.b64encode(final_content_of_file.encode('utf-8'))


    
    api_params=new_content_of_file.strip()[12:].split("')")[0]
    api_url="https://codeless-flask-api.herokuapp.com"+api_params
    print("api="+api_url)

    
    commit_resp=push_to_github(encoded_final_code.decode('utf-8'),sha,git_user)
    commit_status=commit_resp.status_code
    if commit_status==200 or commit_status==201:
        return render_template("API_view.html",api=api_url,new_code=new_content_of_file)
    else:
        return "Commit unsuccessful"
    




if __name__ == "__main__":
    app.run(debug=True)
