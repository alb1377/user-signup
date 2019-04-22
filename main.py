from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup", methods=['POST'])

def set_up():
    username = cgi.escape(request.form['username'])
    user_pw = cgi.escape(request.form['user_pw'])
    user_pw2 = cgi.escape(request.form['user_pw2'])
    user_email = cgi.escape(request.form['user_email'])

    username_error = ""
    user_pw_error = ""
    user_pw2_error = ""
    user_email_error = ""

    if not username:
        print("No Username")
        username_error = "Username is required"
    if not user_pw:
        user_pw_error = "Password is required"
    elif len(user_pw) < 3 or len(user_pw) > 20:
        user_pw_error = "Password must be at least 3 characters long and no longer than 20 characters"
    if user_pw != user_pw2:
        user_pw2_error = "Passwords do not match"
    
    for char in username:
        if char == " ":
            username_error = "Usernames can't contain a space"
    for char in user_pw:
        if char == " ":
            user_pw_error = "Password can't contain a space"
    

    if user_email != "":
        atsymbol = 0 
 
        for char in user_email:
            if char == "@":
                atsymbol += 1
        if atsymbol != 1:
            user_email_error = "Emails contain one @"
        period = 0
        for char in user_email:
            if char == ".":
                period += 1
        if period !=1:
            user_email_error = "Emails contain one ."
        for char in user_email:
           if char == " ":
                user_email_error = "Emails can't contain a space"

        
    if username_error or user_pw_error or user_pw2_error or user_email_error:
        print("An error has occurred")

        return render_template("base1.html", username=username, username_error=username_error, user_pw=user_pw, user_pw_error=user_pw_error, user_pw2=user_pw2, user_pw2_error=user_pw2_error, user_email=user_email, user_email_error=user_email_error)

    return "Thanks for signing up," + " " + username

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/signup", methods=['GET'])
def sign_up_page():
    return render_template("base1.html")

app.run()