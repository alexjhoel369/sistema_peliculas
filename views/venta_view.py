from flask import render_template

def list(ventas):
    return render_template('ventas/index.html',ventas = ventas)

def create(usuarios, peliculas):
    return render_template('ventas/create.html',usuarios=usuarios,peliculas=peliculas)

def edit(venta,usuarios,peliculas):
    return render_template('ventas/edit.html',venta = venta, usuarios=usuarios,peliculas=peliculas)