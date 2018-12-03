import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import datetime
import sqlite3

# Define the database file.
DATABASE = 'BackonLine.db'

# Create an instance of the `Flask` class.
app = Flask(__name__)

# Mail configurations.
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'team6backonline@gmail.com'
app.config['MAIL_DEFAULT_SENDER'] = 'team6backonline@gmail.com'
app.config['MAIL_PASSWORD'] = 'password123?!'

# Create an instance of `Mail` class.
mail = Mail(app)

# Set of allowed file extensions.
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route("/Questions", methods = ['GET', 'POST'])
def questions():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;", [1])
            question_text = cur.fetchall()
            cur.execute("SELECT OptionText, QuestionType, OptionID FROM Options WHERE QuestionID=?;", [1])
            option_data = cur.fetchall()
        except:
            print('There was an error', option_data)
        finally:
            question_text = str(question_text)[3:-4]
            section_text = "Section A: Pain Behaviour"
            conn.close()
            return render_template('questions.html', question_text=question_text, option_data=option_data, section_text=section_text,  question_number=1)
    elif request.method == 'POST':
        questnum = int(request.form['questnum'])
        direction = str(request.form['direction'])
        patient_id = request.form.get('patient_id')
        radio = request.form.get('radio')
        checkbox = request.form.get('checkbox')
        textarea = request.form.get('textarea')
        qhide = request.form.get('qhide')
        skippedqs = int(request.form.get('skippedqs'))
        calc = questnum - 1 - skippedqs
        print(f"{questnum} - {skippedqs} =  {calc}")
        #
        # Insert values.
        # if direction == "forward":
        #     if radio != "":
        #         # Get score and option ID.
        #         if qhide == "false":
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 cur.execute("SELECT OptionID, Score FROM Options WHERE QuestionID=? AND OptionText=?;", [questnum-1, radio])
        #                 OpID_Score = cur.fetchall()
        #             except:
        #                 print('There was an error', login_details)
        #             conn.close()
        #             option_id = OpID_Score[0][0]
        #             score = OpID_Score[0][1]
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [questnum-1])
        #                 duplicate_response = cur.fetchall()
        #             except:
        #                 print('There was an error', login_details)
        #             conn.close()
        #
        #             if duplicate_response != []:
        #                 print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
        #                 try:
        #                     conn = sqlite3.connect(DATABASE)
        #                     cur = conn.cursor()
        #                     cur.execute("DELETE FROM Response Where questionID=?;", [questnum-1])
        #                     conn.commit()
        #                 except:
        #                     print('There was an error', duplicate_response [0][0])
        #                 conn.close()
        #         elif qhide == "true":
        #             calc = questnum - 1 - skippedqs
        #             print(f"{questnum} - {skippedqs} =  {calc}")
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 cur.execute("SELECT OptionID, Score FROM Options WHERE QuestionID=? AND OptionText=?;", [calc, radio])
        #                 OpID_Score = cur.fetchall()
        #             except:
        #                 print('There was an error', login_details)
        #             conn.close()
        #             option_id = OpID_Score[0][0]
        #             score = OpID_Score[0][1]
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [calc])
        #                 duplicate_response = cur.fetchall()
        #             except:
        #                 print('There was an error', login_details)
        #             conn.close()
        #
        #             if duplicate_response != []:
        #                 print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
        #                 try:
        #                     conn = sqlite3.connect(DATABASE)
        #                     cur = conn.cursor()
        #                     cur.execute("DELETE FROM Response Where questionID=?;", [calc])
        #                     conn.commit()
        #                 except:
        #                     print('There was an error', duplicate_response [0][0])
        #                 conn.close()
        #
        #
        #         #print(f"PatientID:{patient_id} direction:{direction} radio:{radio} checkbox:{checkbox} textarea:{textarea} optionID: {option_id} score:{score} questionID:{questnum-1}")
        #         try:
        #             conn = sqlite3.connect(DATABASE)
        #             cur = conn.cursor()
        #             cur.execute("INSERT INTO RESPONSE('patientID', 'optionID', 'questionID', 'score', 'extraInput','date')\
        #             VALUES (?,?,?,?,?,?)",(patient_id,str(option_id),questnum-1,score,"",str(datetime.date.today())))
        #             conn.commit()
        #             print("Record successfully added")
        #         except:
        #             conn.rollback()
        #             print("Error in insert operation")
        #         conn.close()
        #     if checkbox != "[]":
        #         checkbox = checkbox[:-2] + checkbox[-1] #removes last ,
        #         checkbox = checkbox[1:-1] #removes square brackets
        #         checkbox_array = checkbox.split(",") #splits string into array via commas
        #
        #         if qhide == "false":
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 cur.execute("SELECT OptionID FROM Options WHERE QuestionID=?;", [questnum-2])
        #                 Total_OpID= cur.fetchall()
        #             except:
        #                 print('There was an error', Total_OpID)
        #
        #             print(Total_OpID[-1][0])
        #             for index,box in enumerate(checkbox_array):
        #                 box = int(box)
        #                 box = box + Total_OpID[-1][0]
        #                 checkbox_array[index] = box
        #
        #             #Get score and option ID.
        #             for box in checkbox_array:
        #                 print(box)
        #                 try:
        #                     conn = sqlite3.connect(DATABASE)
        #                     cur = conn.cursor()
        #                     cur.execute("SELECT Score FROM Options WHERE QuestionID=? AND OptionID=?;", [questnum-1, box])
        #                     Score = cur.fetchall()
        #                 except:
        #                     print('There was an error', login_details)
        #                 conn.close()
        #                 Score = Score[0][0]
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [questnum-1])
        #                 duplicate_response = cur.fetchall()
        #             except:
        #                 print('There was an error', duplicate_response)
        #             conn.close()
        #
        #             if duplicate_response != []:
        #                 print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
        #                 try:
        #                     conn = sqlite3.connect(DATABASE)
        #                     cur = conn.cursor()
        #                     cur.execute("DELETE FROM Response Where questionID=?;", [questnum-1])
        #                     conn.commit()
        #                 except:
        #                     print('There was an error', duplicate_response [0][0])
        #                 conn.close()
        #             print(patient_id,checkbox_array,questnum-1,Score,"",str(datetime.date.today()))
        #         if qhide == "true":
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 cur.execute("SELECT OptionID FROM Options WHERE QuestionID=?;", [calc])
        #                 Total_OpID= cur.fetchall()
        #             except:
        #                 print('There was an error', Total_OpID)
        #
        #             print(Total_OpID[-1][0])
        #             for index,box in enumerate(checkbox_array):
        #                 box = int(box)
        #                 box = box + Total_OpID[-1][0]
        #                 checkbox_array[index] = box
        #
        #             #Get score and option ID.
        #             for box in checkbox_array:
        #                 print(box)
        #                 try:
        #                     conn = sqlite3.connect(DATABASE)
        #                     cur = conn.cursor()
        #                     cur.execute("SELECT Score FROM Options WHERE QuestionID=? AND OptionID=?;", [calc-1, box])
        #                     Score = cur.fetchall()
        #                 except:
        #                     print('There was an error', login_details)
        #                 conn.close()
        #                 print(Score)
        #                 Score = Score[0][0]
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [calc])
        #                 duplicate_response = cur.fetchall()
        #             except:
        #                 print('There was an error', duplicate_response)
        #             conn.close()
        #
        #             if duplicate_response != []:
        #                 print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
        #                 try:
        #                     conn = sqlite3.connect(DATABASE)
        #                     cur = conn.cursor()
        #                     cur.execute("DELETE FROM Response Where questionID=?;", [calc])
        #                     conn.commit()
        #                 except:
        #                     print('There was an error', duplicate_response [0][0])
        #                 conn.close()
        #             print(patient_id,checkbox_array,questnum-1,Score,"",str(datetime.date.today()))
        #
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 print("test 1")
        #                 cur.execute("INSERT INTO RESPONSE('patientID', 'optionID', 'questionID', 'score', 'extraInput','date')\
        #                 VALUES (?,?,?,?,?,?)",(patient_id,str(checkbox_array),questnum-1,Score,"",str(datetime.date.today())))
        #                 print("test 2")
        #                 conn.commit()
        #                 print("Record successfully added")
        #             except:
        #                 conn.rollback()
        #                 print("Error in insert operation")
        #             conn.close()
        #
        #
        #     if textarea != "":
        #         # Get score and option ID.
        #         try:
        #             conn = sqlite3.connect(DATABASE)
        #             cur = conn.cursor()
        #             cur.execute("SELECT OptionID, Score FROM Options WHERE QuestionID=?;", [questnum-1])
        #             OpID_Score = cur.fetchall()
        #         except:
        #             print('There was an error', login_details)
        #         conn.close()
        #         option_id = OpID_Score[0][0]
        #         score = OpID_Score[0][1]
        #         try:
        #             conn = sqlite3.connect(DATABASE)
        #             cur = conn.cursor()
        #             cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [questnum-1])
        #             duplicate_response = cur.fetchall()
        #         except:
        #             print('There was an error', login_details)
        #         conn.close()
        #
        #         if duplicate_response != []:
        #             print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
        #             try:
        #                 conn = sqlite3.connect(DATABASE)
        #                 cur = conn.cursor()
        #                 cur.execute("DELETE FROM Response Where questionID=?;", [questnum-1])
        #                 conn.commit()
        #             except:
        #                 print('There was an error', duplicate_response [0][0])
        #             conn.close()
        #         try:
        #             conn = sqlite3.connect(DATABASE)
        #             cur = conn.cursor()
        #             cur.execute("INSERT INTO RESPONSE('patientID', 'optionID', 'questionID', 'score', 'extraInput','date')\
        #             VALUES (?,?,?,?,?,?)",(patient_id,str(option_id),questnum-1,score,textarea,str(datetime.date.today())))
        #             conn.commit()
        #             print("Record successfully added")
        #         except:
        #             conn.rollback()
        #             print("Error in insert operation")
        #         conn.close()
       # Load options.
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;", [questnum])
            question_text = cur.fetchall()
            cur.execute("SELECT OptionText, QuestionType, OptionID FROM Options WHERE QuestionID=?;", [questnum])
            option_data = cur.fetchall()
            question_text = str(question_text)[3:-4]
            # Display section name depending on question number.
            if (questnum < 23) and (questnum > 0):
                section_text = "Section A: Pain Behaviour"
            elif (questnum >= 23) and (questnum < 29):
                section_text = "Section B: Back Pain and Work"
            elif (questnum >= 29) and (questnum < 33):
                section_text = "Section C: Back Pain and Lifestyle"
            elif (questnum >= 33) and (questnum < 40):

                section_text = "Section D: Perception of Back Pain";
            elif (questnum >= 40):
                section_text = "Questionaire done";


                section_text = "Section D: Perception of Back Pain"
            elif questnum >= 40:
                # Get the email address of the logged in user via their patient ID which is stored in local storage.
                email = cur.execute("SELECT email FROM Patient WHERE PatientID=?;", [patient_id])
                user_email = cur.fetchall()
                user_email = user_email[0][0]
                # Send confirmation email to user.
                msg = Message("Form submission", recipients=[user_email])
                msg.html = "<h3>Confirmation of form submission</h3>\n<p>This email is to confirm that your BACKonLINE&trade; form has been successfully submitted to your physiotherapist.</p>"
                mail.send(msg)
                return render_template('finish.html', user_email=user_email)
>>>>>>> d6db7cbe4493ca8adb6b15b1d2a3c8622f765974
            return render_template('questions.html', question_text=question_text, option_data=option_data, section_text=section_text, question_number=questnum)
        except:
            print('There was an error')
        finally:
            conn.close()

@app.route("/Welcome", methods = ['GET'])
def welcome_page():
    if request.method =='GET':
        return render_template('welcome.html')

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
            if adminCredentials(login_email, login_password):
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    cur.execute("SELECT PatientID, name FROM Patient WHERE email=?;", [login_email])
                    data = cur.fetchall()
                except:
                    print('There was an error', login_details)
                return render_template('Admin.html', data=data, username=login_email)

            if checkCredentials(login_email, login_password) == 1:
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    cur.execute("SELECT PatientID, name FROM Patient WHERE email=?;", [login_email])
                    data = cur.fetchall()
                except:
                    print('There was an error', login_details)
                resp = make_response(render_template('welcome.html', data=data, username=login_email))
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
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                cur.execute("SELECT PatientID,name FROM Patient WHERE email=?;", [sign_email])
                data = cur.fetchall()
            except:
                print('There was an error', login_details)
            resp = make_response(render_template('welcome.html', data=data, username=sign_email))
        print(f"name: {sign_name}, gender: {sign_gender}, age: {sign_age}, username: {sign_email}, password: {sign_password}")
        return resp
    else:
        username = 'none'
        if 'username' in session:
            username = escape(session['username'])
        return render_template('index.html', msg='', username=username, error="")

# ------------------Methods------------------
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

def adminCredentials(email, password):
    return email == 'admin@admin.com'
    return password == 'admin'

if __name__ == "__main__":
    # Uncomment to use this --> get IPv4 address and go IPv4-address:8080/address-route
    # app.run(host='0.0.0.0', port=8080)
    app.run(debug=True)
