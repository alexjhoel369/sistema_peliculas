from flask import request, redirect,url_for,Blueprint

from models.rol_model import Rol
from views import rol_view

rol_bp = Blueprint ('rol', __name__,url_prefix="/roles")

@rol_bp.route("/")
def index():
    #recupera todos los registros de rols
    roles = Rol.get_all()
    return rol_view.list(roles)

@rol_bp.route("/create", methods=['GET','POST'])
def create():
    if request.method == 'POST':
        rol = request.form['rol']

        rol = Rol(rol)
        rol.save()
        return redirect(url_for('rol.index'))
    
    return rol_view.create()

@rol_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    rol = Rol.get_by_id(id) 
    if not rol:
        return "Rol no encontrado", 404 

    if request.method == 'POST':
        nuevo_rol = request.form['rol']  

        # ACTUALIZAR el rol en la base de datos
        rol.update(rol=nuevo_rol)  
        return redirect(url_for('rol.index'))  

    return rol_view.edit(rol)  

@rol_bp.route("/delete/<int:id>")
def delete(id):
    rol = Rol.get_by_id(id)
    rol.delete()
    return redirect(url_for('rol.index'))