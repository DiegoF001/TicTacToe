from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route("/register", methods=['GET','POST'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmed_password = request.form.get("confirm_password")
        user_pattern = r'(\w){5,12}'
        password_pattern = "^(?=.*?[a-zA-Z])(?=.*?[0-9]).{5,20}$"
        if re.fullmatch(user_pattern, username) is None:
            flash("Username must be 5-12 chars. No special chars.", category='error')
        elif re.match(password_pattern, password) is None:
            flash("Password must be 5-20 chars and contain a number", category='error')
        elif password != confirmed_password:
            flash('Passwords do no match')
        else: 
            flash('Account created successfully', category='sucess')
            return redirect(url_for("auth.login"))
            
    return render_template("register.html")

@auth.route("/logout", methods=['GET','POST'])
def logout():
    pass

@auth.route("/play", methods=['GET','POST'])
def play():
    pass

@auth.route("/scores", methods=['GET'])
def scores():
    pass