from flask import render_template

def render_index(template_name):
    return render_template(template_name)

def render_catalogo(peliculas, query=None):
    return render_template('cliente/catalogo.html', peliculas=peliculas, query=query)

