from flask import request, redirect,url_for,Blueprint

from models.genero_model import Genero
from views import genero_view

genero_bp = Blueprint ('genero', __name__,url_prefix="/generos")

@genero_bp.route("/")
def index():
    #recupera todos los registros de generos
    generos = Genero.get_all()
    return genero_view.list(generos)

@genero_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        genero = request.form['genero']

        genero = Genero(genero)
        genero.save()
        return redirect(url_for('genero.index'))
    
    return genero_view.create()

@genero_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    genero = Genero.get_by_id(id) 
    if not genero:
        return "genero no encontrado", 404 

    if request.method == 'POST':
        nuevo_genero = request.form['genero']  

        # ACTUALIZANDO el genero en la base de datos
        genero.update(genero=nuevo_genero)  
        return redirect(url_for('genero.index'))  

    return genero_view.edit(genero)  

@genero_bp.route("/delete/<int:id>")
def delete(id):
    genero = Genero.get_by_id(id)
    genero.delete()
    return redirect(url_for('genero.index'))