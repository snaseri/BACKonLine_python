import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'BackonLine.db'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

counter = 1

@app.route("/Questions", methods = ['POST', 'GET'])
def questions():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;", [1])
            qdata = cur.fetchall()
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=?;", [1])
            odata = cur.fetchall()
            conn.close()
        except:
            print('There was an error', odata)
            conn.close()
        finally:
            qdata = str(qdata)[3:-4]
            formatted = []
            for i in odata:
                 x = str(i)[2:-3]
                 formatted.append(x)
            conn.close()
            return render_template('questions.html', qdata=qdata, odata=formatted)
    elif request.method == 'POST':
        global counter
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;", [counter])
            qdata = cur.fetchall()
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=?;", [counter])
            odata = cur.fetchall()
            conn.close()
        except:
            print('There was an error', odata)
            conn.close()
        finally:
            qdata = str(qdata)[3:-4]
            formatted = []
            for i in odata:
                 x = str(i)[2:-3]
                 formatted.append(x)
            counter += 1
            conn.close()
            return render_template('questions.html', qdata=qdata, odata=formatted)

@app.route("/index", methods = ['POST'])
def customerAddDetails():
    if request.method =='GET':
        return render_template('index.html')

# =======================================================================
# Sessions

# Cookies login
@app.route("/Login", methods = ['GET','POST'])
def login():
    if request.method=='POST':
        uName = request.form.get('username', default="Error")
        if checkCredentials(uName, pw):
            resp = make_response(render_template('Customer.html', msg='hello '+uName, username=uName))
            resp.set_cookie('username', uName)
            if uName=="Ian":
                user_type = "admin"
                resp.set_cookie('username', uName, 'user-type', user_type)
            else:
                user_type = "customer"
                resp.set_cookie('username', uName, 'user-type', user_type)
        else:
            resp = make_response(render_template('Customer.html', msg='Incorrect  login',username='Guest'))
        return resp
    else:  # if it is a GET
        username = request.cookies.get('username')
        return render_template('index.html', msg='', username=username)

if __name__ == "__main__":
	app.run(debug=True)
