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
        intial_qhide_value = "f,f,f,f,f,f,f,f,f"
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
            return render_template('questions.html', question_text=question_text, option_data=option_data, section_text=section_text,  question_number=1, question_skip=intial_qhide_value)
    elif request.method == 'POST':
        questnum = int(request.form['questnum'])
        direction = str(request.form['direction'])
        patient_id = request.form.get('patient_id')
        radio = request.form.get('radio')
        checkbox = request.form.get('checkbox')
        textarea = request.form.get('textarea')
        qhide = request.form.get('qhide')
        slider = request.form.get('slider')
        skippedqs = int(request.form.get('skippedqs'))
        # Get the selected body part from the body map.
        selected_body_part = request.form.get('selected-body-part')
        # Print the selected slider value.
        print(f"slider = {slider}")
        # Print the selected body part.
        print(f"Body part: {selected_body_part}")
        calc = questnum - 1 - skippedqs
        print(f"{questnum} - 1 - {skippedqs} =  {calc}")
        # Insert values.
        if direction == "forward":
            print(questnum)
            if slider != "":
                    print("This is Q20")
                    # Get score and option ID.
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT OptionID, Score FROM Options WHERE QuestionID=?;", [questnum-1])
                        OpID_Score = cur.fetchall()
                    except:
                        print('There was an error', OpID_Score)
                    conn.close()
                    option_id = OpID_Score[0][0]
                    score = OpID_Score[0][1]
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [questnum-1])
                        duplicate_response = cur.fetchall()
                    except:
                        print('There was an error', duplicate_response)
                    conn.close()
                    if duplicate_response != []:
                        print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
                        try:
                            conn = sqlite3.connect(DATABASE)
                            cur = conn.cursor()
                            cur.execute("DELETE FROM Response Where questionID=?;", [questnum-1])
                            conn.commit()
                        except:
                            print('There was an error', duplicate_response [0][0])
                        conn.close()
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("INSERT INTO RESPONSE('patientID', 'optionID', 'questionID', 'score', 'extraInput','date')\
                        VALUES (?,?,?,?,?,?)",(patient_id,str(option_id),questnum-1,score,str(slider),str(datetime.date.today())))
                        conn.commit()
                        print("Record successfully added")
                    except:
                        conn.rollback()
                        print("Error in insert operation")
                    conn.close()
            if radio != "":
                # Get score and option ID.
                print(f"qhide = {qhide[0]} questnum = {questnum} calc = {calc}")
                print(len(qhide))
                print(f"QHIDE 13 IS {qhide[13]}")
                if (qhide[0] == "t" and calc == 1) or (qhide[14] == "t" and calc == 4) or (qhide[4] == "t" and calc == 5) or (qhide[4] == "t" and calc == 11) or (qhide[6] == "t" and calc == 16) or (qhide[8] == "t" and calc == 18) or (qhide[10] == "t" and calc == 21 ) or (qhide[16] == "t"and calc == 23) or (qhide[12] == "t"and calc == 26):
                    skipped_question = True
                else:
                    skipped_question = False
                if skipped_question == False:
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT OptionID, Score FROM Options WHERE QuestionID=? AND OptionText=?;", [questnum-1, radio])
                        OpID_Score = cur.fetchall()
                    except:
                        print('There was an error', OpID_Score)
                    conn.close()
                    option_id = OpID_Score[0][0]
                    score = OpID_Score[0][1]
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [questnum-1])
                        duplicate_response = cur.fetchall()
                    except:
                        print('There was an error', duplicate_response)
                    conn.close()
                    if duplicate_response != []:
                        print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
                        try:
                            conn = sqlite3.connect(DATABASE)
                            cur = conn.cursor()
                            cur.execute("DELETE FROM Response Where questionID=?;", [questnum-1])
                            conn.commit()
                        except:
                            print('There was an error', duplicate_response [0][0])
                        conn.close()
                elif skipped_question == True:
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT OptionID, Score FROM Options WHERE QuestionID=? AND OptionText=?;", [calc, radio])
                        OpID_Score = cur.fetchall()
                    except:
                        print('There was an error', OpID_Score)
                    conn.close()
                    print(OpID_Score)
                    option_id = OpID_Score[0][0]
                    score = OpID_Score[0][1]
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [calc])
                        duplicate_response = cur.fetchall()
                    except:
                        print('There was an error', duplicate_response)
                    conn.close()

                    if duplicate_response != []:
                        print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
                        try:
                            conn = sqlite3.connect(DATABASE)
                            cur = conn.cursor()
                            cur.execute("DELETE FROM Response Where questionID=?;", [calc])
                            conn.commit()
                        except:
                            print('There was an error', duplicate_response [0][0])
                        conn.close()
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    cur.execute("INSERT INTO RESPONSE('patientID', 'optionID', 'questionID', 'score', 'extraInput','date')\
                    VALUES (?,?,?,?,?,?)",(patient_id,str(option_id),questnum-1,score,"",str(datetime.date.today())))
                    conn.commit()
                    print("Record successfully added")
                except:
                    conn.rollback()
                    print("Error in insert operation")
                conn.close()
            if checkbox != "[]":
                # Removes last.
                checkbox = checkbox[:-2] + checkbox[-1]
                # Removes square brackets.
                checkbox = checkbox[1:-1]
                # Splits string into array via commas.
                checkbox_array = checkbox.split(",")
                print(qhide)
                print(qhide[2])
                if qhide[2] == "t" and calc == 5:
                    skipped_question = True
                else:
                    skipped_question = False
                print(skipped_question)
                if skipped_question == False:
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT OptionID FROM Options WHERE QuestionID=?;", [questnum-2])
                        Total_OpID= cur.fetchall()
                    except:
                        print('There was an error', Total_OpID)
                    print(Total_OpID[-1][0])
                    for index, box in enumerate(checkbox_array):
                        box = int(box)
                        checkbox_array[index] = box
                    # Get score and option ID.
                    for box in checkbox_array:
                        print(box)
                        try:
                            conn = sqlite3.connect(DATABASE)
                            cur = conn.cursor()
                            cur.execute("SELECT Score FROM Options WHERE QuestionID=? AND OptionID=?;", [questnum-1, box])
                            Score = cur.fetchall()
                        except:
                            print('There was an error', Score)
                        conn.close()
                        Score = Score[0][0]
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [questnum-1])
                        duplicate_response = cur.fetchall()
                    except:
                        print('There was an error', duplicate_response)
                    conn.close()
                    if duplicate_response != []:
                        print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
                        try:
                            conn = sqlite3.connect(DATABASE)
                            cur = conn.cursor()
                            cur.execute("DELETE FROM Response Where questionID=?;", [questnum-1])
                            conn.commit()
                        except:
                            print('There was an error', duplicate_response [0][0])
                        conn.close()
                    print(patient_id,checkbox_array,questnum-1,Score,"",str(datetime.date.today()))
                if skipped_question == True:
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT OptionID FROM Options WHERE QuestionID=?;", [calc])
                        Total_OpID= cur.fetchall()
                    except:
                        print('There was an error', Total_OpID)
                    for index,box in enumerate(checkbox_array):
                        box = int(box)
                        checkbox_array[index] = box
                    print(f"checkbox_array = {checkbox_array}")
                    # Get score and option ID.
                    for box in checkbox_array:
                        try:
                            conn = sqlite3.connect(DATABASE)
                            cur = conn.cursor()
                            cur.execute("SELECT Score FROM Options WHERE QuestionID=? AND OptionID=?;", [calc, box])
                            Score = cur.fetchall()
                        except:
                            print('There was an error', Score)
                        conn.close()
                        print(Score)
                        Score = Score[0][0]
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [calc])
                        duplicate_response = cur.fetchall()
                    except:
                        print('There was an error', duplicate_response)
                    conn.close()
                    if duplicate_response != []:
                        print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
                        try:
                            conn = sqlite3.connect(DATABASE)
                            cur = conn.cursor()
                            cur.execute("DELETE FROM Response Where questionID=?;", [calc])
                            conn.commit()
                        except:
                            print('There was an error', duplicate_response [0][0])
                        conn.close()
                    print(patient_id,checkbox_array,questnum-1,Score,"",str(datetime.date.today()))
                if (questnum-1 == 7) or (questnum-1 == 19):
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("INSERT INTO RESPONSE('patientID', 'optionID', 'questionID', 'score', 'extraInput','date')\
                        VALUES (?,?,?,?,?,?)",(patient_id,str(checkbox_array),questnum-1,Score,str(selected_body_part),str(datetime.date.today())))
                        conn.commit()
                        print("Record successfully added")
                    except:
                        conn.rollback()
                        print("Error in insert operation")
                    conn.close()
                else:
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("INSERT INTO RESPONSE('patientID', 'optionID', 'questionID', 'score', 'extraInput','date')\
                        VALUES (?,?,?,?,?,?)",(patient_id,str(checkbox_array),questnum-1,Score,"",str(datetime.date.today())))
                        conn.commit()
                        print("Record successfully added")
                    except:
                        conn.rollback()
                        print("Error in insert operation 250")
                    conn.close()
            if textarea != "":
                # Get score and option ID.
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    cur.execute("SELECT OptionID, Score FROM Options WHERE QuestionID=?;", [questnum-1])
                    OpID_Score = cur.fetchall()
                except:
                    print('There was an error', OpID_Score)
                conn.close()
                option_id = OpID_Score[0][0]
                score = OpID_Score[0][1]
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    cur.execute("SELECT ResponseID FROM Response WHERE questionID=?;", [questnum-1])
                    duplicate_response = cur.fetchall()
                except:
                    print('There was an error', duplicate_response)
                conn.close()
                if duplicate_response != []:
                    print(f"Duplicate ResponseID: {duplicate_response [0][0]}")
                    try:
                        conn = sqlite3.connect(DATABASE)
                        cur = conn.cursor()
                        cur.execute("DELETE FROM Response Where questionID=?;", [questnum-1])
                        conn.commit()
                    except:
                        print('There was an error', duplicate_response [0][0])
                    conn.close()
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    cur.execute("INSERT INTO RESPONSE('patientID', 'optionID', 'questionID', 'score', 'extraInput','date')\
                    VALUES (?,?,?,?,?,?)",(patient_id,str(option_id),questnum-1,score,textarea,str(datetime.date.today())))
                    conn.commit()
                    print("Record successfully added")
                except:
                    conn.rollback()
                    print("Error in insert operation")
                conn.close()
        # Load options.
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT QuestionText FROM Questions WHERE QuestionID=?;", [questnum])
            question_text = cur.fetchall()
            cur.execute("SELECT OptionText, QuestionType, OptionID FROM Options WHERE QuestionID=?;", [questnum])
            option_data = cur.fetchall()
            if (questnum == 3) or (questnum == 20):
                cur.execute("SELECT extraInput FROM Response WHERE QuestionID=? AND PatientID=? AND date=?", [questnum, patient_id, str(datetime.date.today())])
                answered_questions = cur.fetchall()
            else:
                cur.execute("SELECT OptionID FROM Response WHERE QuestionID=? AND PatientID=? AND date=?", [questnum, patient_id, str(datetime.date.today())])
                answered_questions = cur.fetchall()
            question_text = str(question_text)[3:-4]
            # Display section name depending on question number.
            if (questnum < 23) and (questnum > 0):
                section_text = "Section A: Pain Behaviour"
            elif (questnum >= 23) and (questnum < 29):
                section_text = "Section B: Back Pain and Work"
            elif (questnum >= 29) and (questnum < 33):
                section_text = "Section C: Back Pain and Lifestyle"
            elif (questnum >= 33) and (questnum < 40):
                section_text = "Section D: Perception of Back Pain"
            elif (questnum >= 40):
                section_text = "Questionaire done"
                # Get the email address of the logged in user via their patient ID which is stored in local storage.
                email = cur.execute("SELECT email FROM Patient WHERE PatientID=?;", [patient_id])
                user_email = cur.fetchall()
                user_email = user_email[0][0]
                # Send confirmation email to user.
                msg = Message("Form submission", recipients=[user_email])
                msg.html = "<h3>Confirmation of form submission</h3>\n<p>This email is to confirm that your BACKonLINE&trade; form has been successfully submitted to your physiotherapist.</p>"
                mail.send(msg)
                return render_template('finish.html', user_email=user_email)
            return render_template('questions.html', question_text=question_text, option_data=option_data, section_text=section_text, question_number=questnum, question_skip=qhide, ans=answered_questions)
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
        test_value = False
        patient_id = request.get_data().decode('utf8')
        if patient_id[0] == "e":
          patient_id = "No ID"
          login_email = request.form.get('email-login', default="Error")
          login_password = request.form.get('password', default="Error")
        else:
            try:
                conn = sqlite3.connect(DATABASE)
                cur = conn.cursor()
                patient_id = patient_id[12:]
                print(f"pat ID: {patient_id}")
                cur.execute("SELECT email, password FROM Patient WHERE PatientID=?;", [patient_id])
                data = cur.fetchall()
            except:
                print('There was an error')
            print(data)
            login_email = data[0][0]
            login_password = data[0][1]
            print(login_email)
            print(login_password)
            test_value = True

        sign_name = request.form.get('name', default="")
        sign_gender = request.form.get('gender', default="Error")
        sign_age = request.form.get('age', default="Error")
        sign_email = request.form.get('email-signup', default="Error")
        sign_password = request.form.get('email-password', default="Error")
        if sign_password != "Error":
            sign_password = generate_password_hash(sign_password)

        if sign_name == "":
            print("Logging in")
            if adminCredentials(login_email, login_password):
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    cur.execute("SELECT PatientID, name FROM Patient WHERE email=?;", [login_email])
                    data = cur.fetchall()
                except:
                    print('There was an error')
                return render_template('admin.html', data=data, username=login_email, msg='ADMIN', user='admin')
            if checkCredentials(login_email, login_password, test_value) == 1:
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    cur.execute("SELECT PatientID, name FROM Patient WHERE email=?;", [login_email])
                    data = cur.fetchall()
                except:
                    print('There was an error')
                resp = make_response(render_template('welcome.html', data=data, username=login_email))
            elif checkCredentials(login_email, login_password, False) == 2:
                resp = make_response(render_template('index.html', msg='', login_email=login_email, error="Incorrect login"))
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
                print('There was an error')
            resp = make_response(render_template('welcome.html', data=data, username=sign_email))
        print(f"name: {sign_name}, gender: {sign_gender}, age: {sign_age}, username: {sign_email}, password: {sign_password}")
        return resp
    else:
        username = 'none'
        if 'username' in session:
            username = escape(session['username'])
        return render_template('index.html', msg='', username=username, error="")

@app.route("/Patients", methods=['GET'])
def patients():
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT * FROM Patient;")
            patients = cur.fetchall()
            print('Showing patients')
            return render_template('patients.html', error='', patients=patients, user='admin')
        except:
            print('Something went wrong')
        finally:
            conn.close()

@app.route("/getPatientResponses/<patientID>", methods=['GET'])
def patientResponses(patientID):
    print('Loading patient ' + patientID)
    if request.method == 'GET':
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT Questions.QuestionText, Questions.QuestionID, Response.date, Response.extraInput, Response.score, Response.optionID FROM Response INNER JOIN Questions ON Response.questionID=Questions.QuestionID  WHERE Response.PatientID=?;", [patientID])
            response = cur.fetchall()
            print(response)
            optionTextSplit = []
            optionTexts = []
            for i in response:
                for x in i:
                    if isinstance(x, str):
                        if ("[" in x) and ("]" in x):
                            optionText = x.replace('[','')
                            optionText = optionText.replace(']','')
                            optionText = optionText.replace(' ', '')
                            optionTextSplit = optionText.split(',')
                            for m in optionTextSplit:
                                optionTexts.append(m)
                        else:
                            if len(x) < 3 and len(x) > 0:
                                print("xxxxx ",x)
                                optionTexts.append(x)
            print(optionTexts)
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("SELECT OptionID, OptionText FROM Options;")
            option_data = cur.fetchall()


            # optionTrueData = {}
            # for i in option_data:
            #     optionTrueData[i[0]] = i[1]

            optionTrueData = {}
            for i in option_data:
                for t in optionTexts:
                    if (int(t) == i[0]):
                        optionTrueData[t]=i[1]
                        print(optionTrueData)

            print(optionTrueData)
            test_array = []
            test_array2 = []
            for idx, i in enumerate(response):
                test_array2.append(response[idx][5])
                if response[idx][5][0] == "[":
                    test = response[idx][5][1:-1]
                    test = test.split(', ')
                    test_array.append(test)
                else:
                    test_array.append(response[idx][5])

            return render_template('patientresponses.html', error='', response=response, user='admin', optionTrueData=optionTrueData, test_array = test_array,test_array2=test_array2)
        except Exception as e:
            print(e)
            print('Something went wrong with printing responses')
        finally:
            conn.close()
            # ------------------Methods------------------


def checkCredentials(email, password, is_me):
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("SELECT email, password FROM Patient WHERE email=?;", [email])
        login_details = cur.fetchall()
    except:
        print('There was an error', login_details)
    print(f"email: {email} pass: {password}")


    if is_me == False:
        try:
            if email == login_details[0][0] and check_password_hash(login_details[0][1], password):
                return 1
            else:
                return 3
        except:
            return 2
    else:
        try:
            if email == login_details[0][0] and login_details[0][1] == password:
                return 1
            else:
                return 3
        except:
            return 2

def adminCredentials(email, password):
    if email == 'admin@admin.com' and password == 'admin':
        print("Admin login worked")
        return True
    else:
        return False

if __name__ == "__main__":
    app.run(debug=True)
    # Uncomment to use this --> get IPv4 address and go IPv4-address:8080/address-route, and comment out above line.
    # app.run(host='0.0.0.0', port=8080)
