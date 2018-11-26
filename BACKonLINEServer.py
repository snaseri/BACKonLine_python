import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
from flask_mail import Mail, Message
import sqlite3

DATABASE = 'BackonLine.db'

app = Flask(__name__)

app.config['DEBUGGING'] = True
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'team6clientproject@gmail.com'
app.config['MAIL_PASSWORD'] = 'password123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

counter = 1

@app.route("/Questions", methods = ['POST', 'GET'])
def questions():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;", [1])
            question_text = cur.fetchall()
            cur.execute("SELECT OptionText, QuestionType FROM Options WHERE QuestionID=?;", [1])
            option_data = cur.fetchall()
        except:
            print('There was an error', option_data)
        finally:
            question_text = str(question_text)[3:-4]
            section_text = "Section A: Pain Behaviour"
            conn.close()
            return render_template('questions.html', question_text=question_text, option_data=option_data, section_text=section_text)
    elif request.method == 'POST':
        global counter
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;", [counter])
            question_text = cur.fetchall()
            cur.execute("SELECT OptionText,QuestionType FROM Options WHERE QuestionID=?;", [counter])
            option_data = cur.fetchall()
        except:
            print('There was an error', option_data)
        finally:
            question_text = str(question_text)[3:-4]
            if (counter < 23) and (counter > 0):
                section_text = "Section A: Pain Behaviour";
            elif (counter >= 23) and (counter < 29):
                section_text = "Section B: Back Pain and Work";
            elif (counter >= 29) and (counter < 33):
                section_text = "Section C: Back Pain and Lifestyle";
            elif (counter >= 33) and (counter < 40):
                section_text = "Section D: Perception of Back Pain";
            elif (counter >= 40):
                section_text = "Questionaire done";
            counter += 1
            conn.close()
            return render_template('questions.html', question_text=question_text, option_data=option_data, section_text=section_text)

@app.route("/index", methods = ['GET'])
def homepage():
    if request.method =='GET':
        return render_template('index.html')

@app.route("/Welcome", methods = ['GET'])
def welcomepage():
    if request.method =='GET':
        return render_template('welcome.html')

# Cookies login
app.secret_key = 'fj590Rt?h40gg'

# Cookie sessions
@app.route("/Login", methods = ['GET','POST'])
def login():
    if request.method=='POST':
        reminder ="***** REM other pages WILL NOT be able to access the username as they are not set up to use Cookie Sessions *****"
        sign_name = request.form.get('name', default="Error")
        sign_gender = request.form.get('gender', default="Error")
        sign_age = request.form.get('age', default="Error")
        sign_email = request.form.get('email-signup', default="Error")
        sign_password = request.form.get('email-password', default="Error")

        login_email = request.form.get('email-login', default="Error")
        login_password = request.form.get('password', default="Error")
        if sign_name =="":
            print("logging in")
            if checkCredentials(login_email, login_password):
                resp = make_response(render_template('welcome.html', msg='Hello '+login_email+reminder, username=login_email))
            else:
                resp = make_response(render_template('index.html', msg='', login_email = login_email, error = "Incorect Login"))
        if sign_name !="":
            print("signing in")
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute("INSERT INTO PATIENT ('name', 'gender', 'age', 'email', 'password')\
                VALUES (?,?,?,?,?)",(sign_name, sign_gender, sign_age, sign_email, sign_password))
                conn.commit()
                print("Record successfully added")
            except:
                conn.rollback()
                print("error in insert operation")
            resp = make_response(render_template('welcome.html', msg='Hello '+sign_email+reminder, username=sign_email))
        print(f"name: {sign_name}, gender: {sign_gender}, age: {sign_age}, username: {sign_email}, password: {sign_password}")
        return resp
    else:
        username = 'none'
        if 'username' in session:
            username = escape(session['username'])
        return render_template('index.html', msg='', username = username, error = "")

# =================Methods================================
def checkCredentials(email, password):
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT email,password FROM Patient WHERE email=?;", [email])
        login_details = cur.fetchall()
    except:
        print('There was an error', login_details)

    if email == login_details[0][0] and password == login_details[0][1]:
        return True
    else:
        return False

if __name__ == "__main__":
	app.run(debug=True)
