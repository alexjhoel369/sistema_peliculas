from flask import render_template

def list(generos):
    return render_template('admin/generos/index.html',generos = generos)

def create():
    return render_template('admin/generos/create.html')

def edit(genero):
    return render_template('admin/generos/edit.html',genero = genero)

