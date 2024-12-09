from flask import request, redirect, url_for, Blueprint, current_app
from models.pelicula_model import Pelicula
from models.genero_model import Genero
from views import pelicula_view
import os

pelicula_bp = Blueprint('pelicula', __name__, url_prefix="/peliculas")


@pelicula_bp.route("/")
def index():
    # Recupera todos los registros de películas
    peliculas = Pelicula.get_all()
    return pelicula_view.list(peliculas)


@pelicula_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        titulo = request.form['titulo']
        año = request.form['año']
        descripcion = request.form['descripcion']
        idioma = request.form['idioma']
        precio = request.form['precio']
        genero_id = request.form['genero_id']
        file = request.files.get('imagen')  # Obtener el archivo de imagen

        # Guardar la película con la imagen
        pelicula = Pelicula(titulo, año, descripcion, idioma, precio, genero_id)
        pelicula.save(file=file, upload_folder=current_app.config['UPLOAD_FOLDER'])
        return redirect(url_for('pelicula.index'))
    
    generos = Genero.query.all()
    return pelicula_view.create(generos)


@pelicula_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    pelicula = Pelicula.get_by_id(id)
    if request.method == 'POST':
        titulo = request.form['titulo']
        año = request.form['año']
        descripcion = request.form['descripcion']
        idioma = request.form['idioma']
        precio = request.form['precio']
        genero_id = request.form['genero_id']
        file = request.files.get('imagen')  # Obtener el archivo de imagen (si se actualiza)

        # Actualizar la película con los nuevos datos
        pelicula.update(
            titulo=titulo,
            año=año,
            descripcion=descripcion,
            idioma=idioma,
            precio=precio,
            genero_id=genero_id,
            file=file,
            upload_folder=current_app.config['UPLOAD_FOLDER']
        )
        return redirect(url_for('pelicula.index'))
    
    generos = Genero.query.all()
    return pelicula_view.edit(pelicula, generos)


@pelicula_bp.route("/delete/<int:id>")
def delete(id):
    pelicula = Pelicula.get_by_id(id)

    # Eliminar la imagen asociada si existe
    if pelicula.imagen:
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], pelicula.imagen)
        if os.path.exists(image_path):
            os.remove(image_path)  # Eliminar la imagen del sistema de archivos

    pelicula.delete()
    return redirect(url_for('pelicula.index'))
