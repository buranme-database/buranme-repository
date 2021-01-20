from flask import Flask, render_template, request, jsonify
import dbinit   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/profileCompany")
def profileCompany():
    return render_template("profileCompany.html")
    
@app.route("/profileStudent")
def profileStudent():
    return render_template("profileStudent.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/mainPageStudent")
def mainPageStudent():
    return render_template("mainPageStudent.html")
    
@app.route("/mainPageCompany")
def mainPageCompany():
    return render_template("mainPageCompany.html")

@app.route('/ssignup',methods=['POST'])
def ssignup():
    password = request.args.get('password')
    username = request.args.get('username')
    name = request.args.get('name')

    res = dbinit.student_signup(password,username,name)

    ret = {
        "flag":res[0],
        "id":res[1]
    }
    return jsonify(ret)

@app.route('/csignup',methods=['POST'])
def csignup():
    password = request.args.get('password')
    username = request.args.get('username')
    name = request.args.get('name')

    res = dbinit.company_signup(password,username,name)

    ret = {
        "flag":res[0],
        "id":res[1]
    }
    return jsonify(ret)
    
@app.route('/clogin',methods=['POST'])
def clogin():
    username = request.args.get('username')
    password = request.args.get('password')
    res = dbinit.company_login(username,password)
    ret = {
        "flag":res[0],
        "id":res[1]
    }
    return jsonify(ret)

@app.route('/slogin',methods=['POST'])
def slogin():
    username = request.args.get('username')
    password = request.args.get('password')
    res = dbinit.student_login(username,password)
    ret = {
        "flag":res[0],
        "id":res[1]
    }
    return jsonify(ret)

@app.route('/addbranch',methods=['POST'])
def addbranch():
    company_id = request.args.get('company_id')
    name = request.args.get('name')

    res = dbinit.add_branch(company_id,name)

    ret = {
        "flag":res[0],
        "id":res[1]
    }
    return jsonify(ret)

if __name__ == "__main__":
    app.run(debug=True)