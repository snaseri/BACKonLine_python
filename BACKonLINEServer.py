import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'BackonLine.db'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

counter = 1

@app.route("/", methods = ['GET'])
def homepage():
    if request.method == 'GET':
        return render_template('index.html')

@app.route("/Questions", methods = ['POST', 'GET'])
def questions():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;", [1])
            qdata = cur.fetchall()
            #Getting all the different option types with different variable names
            #Getting radiobox options
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=? AND  QuestionType = 'Radiobox' ;", [1])
            rodata = cur.fetchall()
            conn.close()
            #Getting tickbox options
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=? AND  QuestionType = 'Tickbox' ;", [1])
            todata = cur.fetchall()
            conn.close()
            #Getting textbox options
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=? AND  QuestionType = 'Textbox' ;", [1])
            textodata = cur.fetchall()
            conn.close()
            #Getting sliders options
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=? AND  QuestionType = 'Slider' ;", [1])
            sodata = cur.fetchall()
            conn.close()
        except:
            print('There was an error', odata)
            conn.close()
        finally:
            qdata = str(qdata)[3:-4]
            Rformatted = []
            Tformatted = []
            Textformatted = []
            Sformatted = []
            for i in rodata:
                 x = str(i)[2:-3]
                 Rformatted.append(x)
            for i in todata:
                 x = str(i)[2:-3]
                 Tformatted.append(x)
            for i in todata:
                 x = str(i)[2:-3]
                 Textformatted.append(x)
            for i in sodata:
                 x = str(i)[2:-3]
                 Sformatted.append(x)
            conn.close()
            return render_template('questions.html', qdata=qdata, rodata=Rformatted, todata=Tformatted, textodata=Textformatted, sodata=Sformatted)
    elif request.method == 'POST':
        global counter
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;", [counter])
            qdata = cur.fetchall()
            #Getting all the different option types with different variable names
            #Getting radiobox options
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=? AND  QuestionType = 'Radiobox' ;", [counter])
            rodata = cur.fetchall()
            conn.close()
            #Getting tickbox options
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=? AND  QuestionType = 'Tickbox' ;", [counter])
            todata = cur.fetchall()
            conn.close()
            #Getting textbox options
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=? AND  QuestionType = 'Textbox' ;", [counter])
            textodata = cur.fetchall()
            conn.close()
            #Getting sliders options
            cur.execute("SELECT OptionText FROM Options WHERE QuestionID=? AND  QuestionType = 'Slider' ;", [counter])
            sodata = cur.fetchall()
            conn.close()
        except:
            print('There was an error', odata)
            conn.close()
        finally:
            qdata = str(qdata)[3:-4]
            Rformatted = []
            Tformatted = []
            Textformatted = []
            Sformatted = []
            for i in rodata:
                 x = str(i)[2:-3]
                 Rformatted.append(x)
            for i in todata:
                 x = str(i)[2:-3]
                 Tformatted.append(x)
            for i in todata:
                 x = str(i)[2:-3]
                 Textformatted.append(x)
            for i in sodata:
                 x = str(i)[2:-3]
                 Sformatted.append(x)
            conn.close()
            return render_template('questions.html', qdata=qdata, rodata=Rformatted, todata=Tformatted, textodata=Textformatted, sodata=Sformatted)
            counter += 1

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
