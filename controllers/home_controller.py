from flask import Blueprint, render_template,request

from models.pelicula_model import Pelicula
from models.genero_model import Genero

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    peliculas = Pelicula.get_all() 
    return render_template('home/index.html', peliculas=peliculas)

@home_bp.route('/catalogo')
def catalogo():
    peliculas = Pelicula.get_all()
    return render_template('home/catalogo.html', peliculas=peliculas)

@home_bp.route('/generos')
def generos():
    generos = Genero.get_all()  
    genero_id = request.args.get('genero_id', type=int)
    if genero_id:
        peliculas = Pelicula.query.filter_by(genero_id=genero_id).all()
    else:
        peliculas = []
    return render_template('home/generos.html', generos=generos, peliculas=peliculas, genero_id=genero_id)