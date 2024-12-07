from flask import render_template

def list(peliculas):
    return render_template('peliculas/index.html',peliculas = peliculas)

def create(generos):
    return render_template('peliculas/create.html', generos=generos)

def edit(pelicula, generos):
    return render_template('peliculas/edit.html',pelicula = pelicula, generos=generos)