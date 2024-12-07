from flask import request, redirect,url_for,Blueprint
from datetime import datetime

from models.venta_model import Venta
from models.pelicula_model import Pelicula
from models.usuario_model import Usuario

from views import venta_view

venta_bp = Blueprint ('venta', __name__,url_prefix="/ventas")

@venta_bp.route("/")
def index():
    #recupera todos los registros de ventas
    ventas = Venta.get_all()
    return venta_view.list(ventas)

@venta_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        usuario_id = request.form['usuario_id']
        pelicula_id = request.form['pelicula_id']
        fecha_str = request.form['fecha']        

        fecha = datetime.strptime(fecha_str,'%Y-%m-%d').date()

        venta = Venta(usuario_id=usuario_id,pelicula_id=pelicula_id,fecha=fecha)
        venta.save()
        return redirect(url_for('venta.index'))
    
    usuarios = Usuario.query.all()
    peliculas = Pelicula.query.all()

    return venta_view.create(usuarios, peliculas)