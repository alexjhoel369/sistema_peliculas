from flask import render_template

def render_login_form():
    return render_template("auth/login.html")

def render_register_form():
    return render_template("auth/register.html")
