import json
from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route("/tomacho-home")
def homepage():
    return render_template('homePage.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/projects/3Es")
def tresEs():
    return render_template('/projects/3EsPLN/templates/3Ehome.html')

@app.route("/projects/3Es/combination")
def tresEsComb():
    return render_template('/projects/3EsPLN/templates/3Ecombination.html')

@app.route("/layout")
def layout():
    return render_template('layout.html')

# @app.route("/api/termos")
# def termos_api():
#     jsonfile = json.load(dbFile)
#     return json.dump(jsonfile)

app.run(host="localhost", port=4002, debug=True)