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
    password = request.form["password"]
    password_validate = request.form["password_validate"]
    email = request.form["email"]

    username_error = ''
    password_error = ''
    password_validate_error = ''
    pw_error = ''
    email_error = ''

    if len(username) < 3:
        username = ''
        username_error = "Invalid username. Must be no fewer than 3 characters and no longer than 20 characters"
    elif len(username) > 20:
        username = ''
        username_error = "Invalid username. Must be no fewer than 3 characters and no longer than 20 characters"
    else:
        username = username

    if len(password) < 3:
        password = ""
        password_error = "Invalid password. Must be no fewer than 3 and no longer than 20 characters"

    if len(password_validate) < 3:
        password_validate = ""
        password_validate_error = "Passwords do not match"

    if len(password) > 20:
        password = ""
        password_error = "Invalid password. Must be no fewer than 3 and no longer than 20 characters"

    if len(password_validate) > 20:
        password_validate = ""
        password_validate_error = "Passwords do not match"   

    if password != password_validate:
        password = ""
        password_validate = ""
        pw_error = "Passwords do not match"
    if len(email) > 0:
        if not(email.endswith('@') or email.startswith('@') or email.endswith('.') or email.startswith('.')) and email.count('@') == 1 and email.count('.') == 1:
            email=email
        else:
            email = ''
            email_error = "Invalid email" 
    else:
        email = ''

    if username == "":
        username_error = "Invalid username. Must be no fewer than 3 characters and no longer than 20 characters"
    if password == "":
        password_error = "Invalid password. Must be no fewer than 3 and no longer than 20 characters"
    if password_validate == "":
        password_validate_error = "Passwords do not match"


    if not username_error and not pw_error and not password_error and not password_validate_error and not email_error:
        return render_template('welcome.html', username = username)

    else:
        return render_template('main.html', pw_error=pw_error, username_error=username_error, password_error=password_error, password_validate_error=password_validate_error, email_error=email_error,
        username=username, password=password, password_validate=password_validate, email=email)

app.run()