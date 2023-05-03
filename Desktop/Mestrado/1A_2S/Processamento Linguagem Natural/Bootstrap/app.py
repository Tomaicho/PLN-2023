import json
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')

file = open('terms.json')
db = json.load(file)

@app.route("/term/<t>")
def term(t):
    return render_template('term.html', designation=t, value=db.get(t,"None"))

@app.route("/term", methods=["POST"])
def addTerm():
    designation = request.form["designation"]
    description = request.form["description"]
    # print(designation, description)
    if designation not in db:
        db[designation] = {"desc":description}
        file_save = open("terms_copy.json", 'w')
        json.dump(db, file_save, ensure_ascii=False, indent=4)
        info_message = "Term added successfuly!"
    else:
        info_message = "Term already exists!"

    return render_template('terms.html', designations=db.keys(), message=info_message)

@app.route("/term/<designation>", methods=["DELETE"])
def deleteTerm(designation):
    desc = db[designation]
    if designation in db:
        del db[designation]
        file_save = open("terms_copy.json", 'w')
        json.dump(db, file_save, ensure_ascii=False, indent=4)

    return {designation: {"desc": desc}}


@app.route("/terms")
def terms():
    return render_template('terms.html', designations=db.keys())

@app.route("/")
def layout():
    return render_template('layout.html', title="Welcome!!")

# @app.route("/api/termos")
# def termos_api():
#     jsonfile = json.load(dbFile)
#     return json.dump(jsonfile)

app.run(host="localhost", port=4002, debug=True)