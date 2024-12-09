from flask import Blueprint, redirect, url_for, session, flash
from views.admin_view import render_dashboard
from .auth_controller import login_required

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.before_request
@login_required
def verificar_acceso():
    # Verificar si el usuario es administrador (rol_id == 1)
    if session.get("user_role") != 1:
        flash("Acceso denegado. Debes ser admin para acceder caiman.", "danger")
        return redirect(url_for("auth.login"))

# Ruta principal del dashboard
@admin_bp.route("/")
def dashboard():
    return render_dashboard()

# Rutas (redirigen a sus respectivos blueprints)
@admin_bp.route("/roles/")
def roles():
    return redirect(url_for("rol.index"))

@admin_bp.route("/usuarios/")
def usuarios():
    return redirect(url_for("usuario.index"))

@admin_bp.route("/generos/")
def generos():
    return redirect(url_for("genero.index"))

@admin_bp.route("/peliculas/")
def peliculas():
    return redirect(url_for("pelicula.index"))

@admin_bp.route("/ventas/")
def ventas():
    return redirect(url_for("venta.index"))
