from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
def login():
    return render_template("login.html")

@views.route("/logout")
def logout():
    return render_template("scores.html")

@views.route("/register")
def register():
    return render_template("register.html")

@views.route("/play")
def play():
    return render_template("play.html")

@views.route("/scores")
def scores():
    return render_template("scores.html")