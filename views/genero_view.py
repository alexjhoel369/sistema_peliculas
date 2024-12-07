from flask import render_template

def list(generos):
    return render_template('generos/index.html',generos = generos)

def create():
    return render_template('generos/create.html')

def edit(genero):
    return render_template('generos/edit.html',genero = genero)