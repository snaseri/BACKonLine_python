import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import sqlite3

DATABASE = 'BackonLine.db'

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'team6backonline@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'team6backonline@gmail.com'
app.config['MAIL_PASSWORD'] = 'password123?!'

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
    msg = Message("Form submission", recipients=["team6backonline@gmail.com"])
    msg.html = "<h3>Confirmation of form submission</h3>\n<p>This email is to confirm that your BACKonLINE&trade; form has been successfully submitted to your physiotherapist.</p>"
    mail.send(msg)
    if request.method =='GET':
        return render_template('index.html')

@app.route("/Welcome", methods = ['GET'])
def welcomepage():
    if request.method =='GET':
        return render_template('welcome.html')

# IN PROGRESS DON'T DELETE
# @app.route("/PersonalData", methods = ['GET'])
# def personal_data_page():
#     if checkCredentials(email):
#         if request.method == 'GET':
#             try:
#                 conn = sqlite3.connect(DATABASE)
#                 cur = conn.cursor()
#                 email = cur.execute("SELECT name,gender,age,email FROM Patient WHERE email=?;", [email])
#                 resp = make_response(render_template('Personal_Data.html', msg='name: ' + name + ' age: ' + age + 'gender: ' + gender + 'email: ' + email, username=email))
#             except:
#                 conn.rollback()
#                 print("Error in insert operation")
#             resp = make_response(render_template('Personal_Data.html', msg='Personal data could not load', username=email))
#          return resp

# Cookie sessions
@app.route("/Login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        sign_name = request.form.get('name', default="Error")
        sign_gender = request.form.get('gender', default="Error")
        sign_age = request.form.get('age', default="Error")
        sign_email = request.form.get('email-signup', default="Error")
        sign_password = request.form.get('email-password', default="Error")
        sign_password = generate_password_hash(sign_password)
        login_email = request.form.get('email-login', default="Error")
        login_password = request.form.get('password', default="Error")
        if sign_name == "":
            print("Logging in")
            if checkCredentials(login_email, login_password) == 1:
                resp = make_response(render_template('welcome.html', msg='Hello ' + login_email, username=login_email))
            elif checkCredentials(login_email, login_password) == 2:
                resp = make_response(render_template('index.html', msg='', login_email=login_email, error="Incorect login"))
            else:
                resp = make_response(render_template('index.html', msg='', login_email=login_email, error="Incorrect login"))
        if sign_name != "":
            print("Signing in")
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute("INSERT INTO PATIENT ('name', 'gender', 'age', 'email', 'password')\
                VALUES (?,?,?,?,?)",(sign_name, sign_gender, sign_age, sign_email, sign_password))
                conn.commit()
                print("Record successfully added")
            except:
                conn.rollback()
                print("Error in insert operation")
            resp = make_response(render_template('welcome.html', msg='Hello '+sign_email, username=sign_email))
        print(f"name: {sign_name}, gender: {sign_gender}, age: {sign_age}, username: {sign_email}, password: {sign_password}")
        return resp
    else:
        username = 'none'
        if 'username' in session:
            username = escape(session['username'])
        return render_template('index.html', msg='', username=username, error="")

# =================Methods================================
def checkCredentials(email, password):
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT email, password FROM Patient WHERE email=?;", [email])
        login_details = cur.fetchall()
    except:
        print('There was an error', login_details)
    try:
        if email == login_details[0][0] and check_password_hash(login_details[0][1], password):
            return 1
        else:
            return 3
    except:
        return 2

if __name__ == "__main__":
	app.run(debug=True)
