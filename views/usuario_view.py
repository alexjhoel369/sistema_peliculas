from flask import render_template

def list(usuarios):
    return render_template('usuarios/index.html',usuarios = usuarios)

def create(roles):
    return render_template('usuarios/create.html', roles=roles)

def edit(usuario, roles):
    return render_template('usuarios/edit.html', usuario=usuario, roles=roles)