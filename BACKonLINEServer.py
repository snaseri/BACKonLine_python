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
        uName = request.form.get('username', default="Error")
        pw = request.form.get('password', default="Error")
        if checkCredentials(uName, pw):
            resp = make_response(render_template('welcome.html', msg='Hello '+uName+reminder, username=uName))
            # session['username'] = request.form['username']
            # session['Password'] = 'pa55wrd'
        else:
            resp = make_response(render_template('welcome.html', msg='Incorrect login',username='Guest'))
        return resp
    else:
        username = 'none'
        if 'username' in session:
            username = escape(session['username'])
        return render_template('index.html', msg='', username = username)

# =================Methods================================
def checkCredentials(uName, pw):
    return pw == 'admin'

if __name__ == "__main__":
	app.run(debug=True)
