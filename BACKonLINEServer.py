import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'BACKonLINE.sql'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/Questions", methods = ['POST','GET'])
def studentAddDetails():
	if request.method =='GET':
		return render_template('Questions.html')
	if request.method =='POST':
		OptionID = request.form.get('OptionID', default="Error")#rem: args for get form for post
		QuestionID = request.form.get('QuestionID', default="Error")
#		PatientID = request.form.get('PatientID', default="Error" to be added after login made
		print("inserting student"+OptionID)
		try:
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			cur.execute("INSERT INTO Response ('OptionID',)\ #Patient ID to be added
						VALUES (?,?)",(OptionID, QuestionID) )

			conn.commit()
			msg = "Record successfully added"
		except:
			conn.rollback()
			msg = "error in insert operation"
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
            resp = make_response(render_template('Customer.html', msg='hello '+uName, username = uName))
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
        return render_template('index.html', msg='', username = username)


#       methods
def checkCredentials(uName, pw):
    return pw == 'ian'

# =======================================================================
#      the db creation methods
