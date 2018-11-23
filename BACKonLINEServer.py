import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'BackonLine.db'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/Questions", methods = ['POST','GET'])
def studentAddDetails():
	# if request.method =='GET':
	# 	return render_template('Questions.html')
	if request.method =='GET':
		try:
			questionid = '1'#request.form.get('name', default="Error") #rem: args for get form for post
			conn = sqlite3.connect(DATABASE)
			cur = conn.cursor()
			# cur.execute("SELECT * FROM Students WHERE surname=? AND public = 'True';", [surname])
			#AND  public = 'True'
			cur.execute("SELECT * FROM Options WHERE QuestionID=? ;", [questionid])
			data = cur.fetchall()
			print(data)
		except:
			print('there was an error', data)
			conn.close()
		finally:
			conn.close()
			#return str(data)
			return render_template('Questions.html', data = data)

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
# @app.route("/Login", methods = ['GET','POST'])
# def login():
#     if request.method=='POST':
#         uName = request.form.get('username', default="Error")
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
#         return render_template('index.html', msg='', username = username)
#
#
# #       methods
# def checkCredentials(uName, pw):
#     return pw == 'ian'
#
# # =======================================================================
# #      the db creation methods

if __name__ == "__main__":
	app.run(debug=True)
	#app.run(host='0.0.0.0', port=8080)
