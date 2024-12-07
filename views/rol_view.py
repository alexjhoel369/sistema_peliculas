from flask import render_template

def list(roles):
    return render_template('roles/index.html',roles = roles)

def create():
    return render_template('roles/create.html')

def edit(rol):
    return render_template('roles/edit.html',rol = rol)