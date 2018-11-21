import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'BACKonLINE.sql'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

<<<<<<< HEAD
@app.route("/Questions")
def questions():
    return render_template('questions.html')

@app.route("/Login")
def login():
    return render_template('index.html')

#---------------------------------------------------------------#
#Ian's code below to be deleted but usefull as reference for now#
#---------------------------------------------------------------#
@app.route("/Admin")
def admin():
    username = request.cookies.get('username')
    return render_template('Admin.html', msg = '', username = username)


@app.route("/Customer")
def customer():
    username = request.cookies.get('username')
    return render_template('Customer.html', msg = '', username = username)
=======
>>>>>>> 1e3e3594af7ced7b175cbb71c656d0b5a4fa5db6

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
<<<<<<< HEAD
# @app.route("/Login", methods = ['GET','POST'])
# def login():
#     if request.method=='POST':
#         uName = request.form.get('username', default="Error")
#         pw = request.form.get('password', default="Error")
#         if checkCredentials(uName, pw):
#             resp = make_response(render_template('Customer.html', msg='hello '+uName, username = uName))
#             resp.set_cookie('username', uName)
#             if uName=="Ian":
#                 user_type = "admin"
#                 resp.set_cookie('username', uName, 'user-type', user_type)
#             else:
#                 user_type = "customer"
#                 resp.set_cookie('username', uName, 'user-type', user_type)
#         else:
#             resp = make_response(render_template('Customer.html', msg='Incorrect  login',username='Guest'))
#         return resp
#     else:  # if it is a GET
#         username = request.cookies.get('username')
#         return render_template('Login.html', msg='', username = username)
#
#     if uName=="Ian":
#         user_type = "admin"
#         resp.set_cookie('username', uName, 'user-type', user_type)
#     else:
#         user_type = "customer"
#         resp.set_cookie('username', uName, 'user-type', user_type)


# Cookie sessions
# set the secret key.  keep this really secret:
app.secret_key = 'fj590Rt?h40gg'

# Cookie sessions
# @app.route("/Login", methods = ['GET','POST'])
# def login():
#     if request.method=='POST':
#         reminder =". ***** REM other pages WILL NOT be able to access the username as they are not set up to use Cookie Sessions. "
#         uName = request.form.get('username', default="Error")
#         pw = request.form.get('password', default="Error")
#         if checkCredentials(uName, pw):
#             resp = make_response(render_template('Customer.html', msg='hello '+uName+reminder, username = uName))
#             session['username'] = request.form['username']
#             session['Password'] = 'pa55wrd'
#             # session['data'] = 'The mayor of London has claimed Volkswagen should pay £2.5m for missed congestion charge payments following the emissions-rigging scandal. Sadiq Khan said 80,000 VW engines fitted with "defeat devices" were registered in London.The devices, which detect when an engine is being tested, changed performance to improve results.VW, the biggest carmaker in the world, admitted about 11 million cars worldwide were fitted with the device.Transport for London calculated the £2.5m figure from the number of owners of affected VW vehicles claiming a discount for which they were not entitled."If you dont ask you dont get. Im a champion for clean air, Im a champion for London," said Mr Khan.'
#         else:
#             resp = make_response(render_template('Customer.html', msg='Incorrect  login',username='Guest'))
#         return resp
#     else:
#         username = 'none'
#         if 'username' in session:
#             username = escape(session['username'])
#         return render_template('Login.html', msg='', username = username)
=======
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
>>>>>>> 1e3e3594af7ced7b175cbb71c656d0b5a4fa5db6


#       methods
def checkCredentials(uName, pw):
    return pw == 'ian'

# =======================================================================
#      the db creation methods
