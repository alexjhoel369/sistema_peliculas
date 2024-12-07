from flask import request, redirect,url_for,Blueprint
from datetime import datetime

from models.usuario_model import Usuario
from models.rol_model import Rol

from views import usuario_view

usuario_bp = Blueprint ('usuario', __name__,url_prefix="/usuarios")

@usuario_bp.route("/")
def index():
    #recupera todos los registros de los usuarios
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)

@usuario_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        rol_id = request.form['rol_id']

        usuario = Usuario(username, password, nombre, apellido, email, telefono, fecha, rol_id)
        usuario.save()
        return redirect(url_for('usuario.index'))
    
    roles = Rol.query.all()
    
    return usuario_view.create(roles)


@usuario_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    usuario = Usuario.get_by_id(id)
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] if 'password' in request.form else None
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        rol_id = request.form['rol_id']

        usuario.update(username, password, nombre, apellido, email, telefono, fecha, rol_id)
        return redirect(url_for('usuario.index'))
    
    roles = Rol.query.all()
    return usuario_view.edit(usuario, roles)


@usuario_bp.route("/delete/<int:id>")
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))