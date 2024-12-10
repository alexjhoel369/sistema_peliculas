from flask import Blueprint, render_template, request
from models.pelicula_model import Pelicula
from models.genero_model import Genero

# Blueprint para el home
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    peliculas = Pelicula.get_all()  # Obtiene todas las películas
    if not peliculas:
        peliculas = []  # Garantiza que haya una lista vacía en caso de error
    return render_template('home/index.html', peliculas=peliculas)

@home_bp.route('/catalogo')
def catalogo():
    peliculas = Pelicula.get_all()
    return render_template('home/catalogo.html', peliculas=peliculas)

@home_bp.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('q', '').strip().lower()
    peliculas = []

    if query:
        peliculas = Pelicula.query.filter(
            Pelicula.titulo.ilike(f'%{query}%')
        ).all()

    return render_template('home/catalogo.html', peliculas=peliculas, query=query)


@home_bp.route('/generos')
def generos():
    generos = Genero.get_all()  # Obtenemos todos los géneros
    genero_id = request.args.get('genero_id', type=int)

    # Obtenemos películas según el género seleccionado
    peliculas = Pelicula.query.filter_by(genero_id=genero_id).all() if genero_id else []

    return render_template(
        'home/generos.html',
        generos=generos,
        peliculas=peliculas,
        genero_id=genero_id
    )
