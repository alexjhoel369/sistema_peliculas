from flask import render_template

def list(ventas):
    return render_template('admin/ventas/index.html',ventas = ventas)

def create(usuarios, peliculas):
    return render_template('admin/ventas/create.html',usuarios=usuarios,peliculas=peliculas)

def edit(venta,usuarios,peliculas):
    return render_template('admin/ventas/edit.html',venta = venta, usuarios=usuarios,peliculas=peliculas)


