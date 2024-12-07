from flask import Blueprint, render_template, session, redirect, url_for, flash
from functools import wraps
from models.usuario_model import Usuario

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user_id = session.get("user_id")
        if not user_id:
            flash("Debes iniciar sesión para acceder a esta página.", "warning")
            return redirect(url_for("auth.login"))
        
        usuario = Usuario.query.get(user_id)
        if usuario.rol_id != 1:  
            flash("No tienes permiso para acceder a esta página.", "danger")
            return redirect(url_for("home.index"))
        
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route("/dashboard")
@admin_required
def dashboard():
    return render_template("admin/base.html") 
