from flask import request, redirect,url_for,Blueprint,session,flash
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

@venta_bp.route("/create_from_index", methods=['POST'])
def create_from_index():
    if 'user_id' not in session:  # Verificamos si el usuario está autenticado
        flash("Debes iniciar sesión para realizar una compra.", "warning")
        return redirect(url_for('auth.login'))

    # Obtenemos datos del formulario
    pelicula_id = request.form.get('pelicula_id')
    usuario_id = session['user_id']  # Obtenemos el ID del usuario actual desde la sesión
    fecha = datetime.now().date()  # Fecha actual

    # Validar si la película existe
    pelicula = Pelicula.get_by_id(pelicula_id)
    if not pelicula:
        flash("La película seleccionada no existe.", "danger")
        return redirect(url_for('client.index'))  # Redirigir a la página principal del cliente

    # Crear la venta
    venta = Venta(usuario_id=usuario_id, pelicula_id=pelicula_id, fecha=fecha)
    venta.save()

    flash(f"¡Compra exitosa de '{pelicula.titulo}'!", "success")
    return redirect(url_for('client.index'))  # Redirige a la página principal del cliente


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

@venta_bp.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    venta = Venta.get_by_id(id)
    if request.method == 'POST':
        usuario_id = request.form['usuario_id']
        pelicula_id = request.form['pelicula_id']
        fecha_str = request.form['fecha']        

        fecha = datetime.strptime(fecha_str,'%Y-%m-%d').date()
        #ACTUALIZAR
        venta.update(usuario_id=usuario_id,pelicula_id=pelicula_id,fecha=fecha)
        return redirect(url_for('venta.index'))
    
    usuarios = Usuario.query.all()
    peliculas = Pelicula.query.all()
    return venta_view.edit(venta,usuarios,peliculas)

@venta_bp.route("/delete/<int:id>")
def delete(id):
    venta = Venta.get_by_id(id)
    venta.delete()
    return redirect(url_for('venta.index'))