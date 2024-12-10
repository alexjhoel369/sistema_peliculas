from flask import Blueprint, redirect, url_for, render_template, session, flash, request
from models.pelicula_model import Pelicula
from models.genero_model import Genero
from .auth_controller import login_required

client_bp = Blueprint("client", __name__, url_prefix="/client")

@client_bp.before_request
@login_required
def verificar_acceso_cliente():
    # Verificar si el usuario es cliente (rol_id == 2)
    if session.get("user_role") != 2:
        flash("Acceso denegado. Debes ser cliente para acceder caiman.", "danger")
        return redirect(url_for("auth.login"))

# Ruta principal del cliente (la página principal del cliente)
@client_bp.route("/")
def index():
    peliculas = Pelicula.query.all()
    # Si no hay películas
    if not peliculas:
        peliculas = []
    # Pasamos 'peliculas' al template
    return render_template("cliente/index.html", peliculas=peliculas)

@client_bp.route('/catalogo')
def catalogo():
    peliculas = Pelicula.get_all()
    return render_template('cliente/catalogo.html', peliculas=peliculas)

@client_bp.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('q', '').strip().lower()
    peliculas = []

    if query:
        peliculas = Pelicula.query.filter(
            Pelicula.titulo.ilike(f'%{query}%')
        ).all()

    return render_template('cliente/catalogo.html', peliculas=peliculas, query=query)

@client_bp.route("/generos")
def generos():
    generos = Genero.query.all()  
    genero_id = request.args.get('genero_id', type=int)  
    peliculas = Pelicula.query.filter_by(genero_id=genero_id).all() if genero_id else []  
    return render_template(
        'cliente/generos.html',  
        generos=generos,
        peliculas=peliculas,
        genero_id=genero_id
    )
