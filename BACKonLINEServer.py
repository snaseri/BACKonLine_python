import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
counter = 1

@app.route("/Questions", methods = ['POST','GET'])
def questions():

    if request.method == 'GET':
        global counter
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;",[counter])
            data = cur.fetchall()
            conn.close()
        except:
            print('There was an error', data)
            conn.close()
        finally:
            data = str(data)[3:-4]
            conn.close()
            counter+=1
            return render_template('Questions.html', data=data)

    if request.method =='POST':
        OptionID = request.form.get('OptionID', default="Error")#rem: args for get form for post
        QuestionID = request.form.get('QuestionID', default="Error")
#       PatientID = request.form.get('PatientID', default="Error" to be added after login made
        print("inserting student"+OptionID)
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("INSERT INTO Response ('OptionID',)\
                        VALUES (?,?)",(OptionID, QuestionID) ) #Patient ID to be added
            conn.commit()
            msg = "Response successfully stored"
        except:
            conn.rollback()
            msg = "Error in insert operation"
        finally:
            conn.close()
            return msg

@app.route("/index")
def customerDetailsForm():
    username = request.cookies.get('username')
    return render_template('CustomerData.html', username = username)

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

#       methods
def checkCredentials(uName, pw):
    return pw == 'ian'

#This is important it allows the server to run -- don't delete
if __name__ == "__main__":
    app.run(debug=True)
