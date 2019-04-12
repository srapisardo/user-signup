from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('main.html')

@app.route("/", methods=['POST'])
def validate_fields():
    username = request.form["username"]
    pw1 = request.form["pw1"]
    pw2 = request.form["pw2"]
    email = request.form["email"]

    username_error = ''
    pw1_error = ''
    pw2_error = ''
    pw_error = ''
    email_error = ''

    if len(username) < 3:
        username = ''
        username_error = 'Username must be more than 3 characters'
    elif len(username) > 20:
        username = ''
        username_error = 'Username must be less than 20 characters'
    else:
        username = username

    if len(pw1) < 3:
        pw1 = pw1
        pw1_error = 'Password must contain more than 3characters long, 20 max, minimum 14 recommended'

    if len(pw2) < 3:
        pw2 = pw2
        pw2_error = 'Verification password must contain more than 3 characters long, 20 max, minimum 14 recommended' 

    if len(pw1) > 20:
        pw1 = pw1
        pw1_error = 'Password is too long, 20 max, minimum 14 recommended'

    if len(pw2) > 20:
        pw2 = pw2
        pw2_error = 'Verification password is too long, 20 max, minimum 14 recommended'    

    if pw1 != pw2:
        pw1 = pw1
        pw2 = pw2
        pw_error = 'Passwords do not match'
    if len(email) > 0:
        if not(email.endswith('@') or email.startswith('@') or email.endswith('.') or email.startswith('.')) and email.count('@') == 1 and email.count('.') == 1:
            email=email
        else:
            email = ''
            email_error = 'Improperly formed email  -- it must contain an @ sign, only one period, and is between 3 and 20 characters long'
    else:
        email = ''

    if username == "":
        username_error = 'Username must be more than 3 characters but no more than 20'
    if pw1 == "":
        pw1_error = 'Set a password, no fewer than 3 and no longer than 20 characters'
    if pw2 == "":
        pw2_error = 'Enter a password to match the one above, no fewer than 3 and no longer than 20 characters'


    if not username_error and not pw_error and not pw1_error and not pw2_error and not email_error:
        return render_template('welcome.html', username = username)

    else:
        return render_template('main.html', pw_error=pw_error, username_error=username_error, pw1_error=pw1_error, pw2_error=pw2_error, email_error=email_error,
        username=username, pw1=pw1, pw2=pw2, email=email)

app.run()