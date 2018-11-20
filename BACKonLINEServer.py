import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'database.db'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route("/Admin")
def admin():
    username = request.cookies.get('username')
    return render_template('Admin.html', msg = '', username = username)

@app.route("/Customer")
def customer():
    username = request.cookies.get('username')
    return render_template('Customer.html', msg = '', username = username)

@app.route("/Customer/AddDetails")
def customerDetailsForm():
    username = request.cookies.get('username')
    return render_template('CustomerData.html', username = username)

@app.route("/Customer/addCustomer", methods = ['POST'])
def customerAddDetails():
    firstName = request.form.get('firstName', default="Error")#rem: args for get form for post
    surname = request.form.get('surname', default="Error")
    termLocation = request.form.get('termLocation', default="Error")
    homeLocation = request.form.get('homeLocation', default="Error")
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO Customers ('firstName', 'surname', 'termLocation', 'homeLocation')\
                     VALUES (?,?,?,?)",(firstName, surname, termLocation, homeLocation) )
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        return msg
        conn.close()

# =======================================================================
# Sessions

# Cookies login
@app.route("/Login", methods = ['GET','POST'])
def login():
    if request.method=='POST':
        uName = request.form.get('username', default="Error")
        pw = request.form.get('password', default="Error")
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
        return render_template('Login.html', msg='', username = username)

    if uName=="Ian":
        user_type = "admin"
        resp.set_cookie('username', uName, 'user-type', user_type)
    else:
        user_type = "customer"
        resp.set_cookie('username', uName, 'user-type', user_type)


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


# =======================================================================
#       methods
def checkCredentials(uName, pw):
    return pw == 'ian'

# =======================================================================
#      the db creation methods
def deleteTables():
    conn = sqlite3.connect(DATABASE)
    conn.execute('DROP TABLE IF EXISTS Jobs')
    conn.execute('DROP TABLE IF EXISTS Orders')
    conn.execute('DROP TABLE IF EXISTS Customers')
    conn.close()

def populateCustomers():
    conn = sqlite3.connect(DATABASE)
    customers = [('Ian','Cooper','Cardiff',  'Devon'),
                 ('Chris','Gwilliams','Cardiff',  'asdfs'),
                 ('Dave','Shepard','Forest',  'fghdf'),
                 ('Wendy','Ivins','sdfsdf', 'sdfsdf')  ]
    conn.executemany("INSERT INTO `Customers`(`firstName`,`surname`, 'termLocation', 'homeLocation' )\
                    VALUES (?,?,?,?)",customers)
    conn.commit()
    conn.close()

def populateJobs():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    jobs = [('Oil Change','Change the Oil'),
            ('MOT','Do the MOT'),
            ('Oil and Filter ','Charge More')]
    cur.executemany("INSERT INTO Jobs ('name','description') VALUES (?,?)",jobs)
    conn.commit()
    conn.close()

def populateOrders():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    orders = [(1,3),(1,2),(3,3),(2,1)]
    cur.executemany("INSERT INTO Orders ('jobID','customerID') VALUES (?,?)",orders)
    conn.commit()
    conn.close()

def createDB():
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE IF NOT EXISTS `Customers` (\
                            `ID`INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
                            `firstName`TEXT NOT NULL,\
                            `surname`TEXT NOT NULL,\
                            `termLocation`TEXT NOT NULL,\
                            `homeLocation` TEXT NOT NULL,\
                            `public` TEXT DEFAULT True);')
    conn.execute('CREATE TABLE IF NOT EXISTS `Jobs` (\
                              `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
                              `name` TEXT NOT NULL,\
                            `description` Text);')
    conn.execute('CREATE TABLE IF NOT EXISTS `Orders` (\
                            orderID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
                            jobID INTEGER NOT NULL,\
                            customerID INTEGER NOT NULL);')
    print ("Tables now exist");
    conn.close()

if __name__ == "__main__":
    deleteTables()
    createDB()
    populateCustomers()
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080)
