from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from functools import wraps
from models.usuario_model import Usuario
from database import db

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Decorador para rutas protegidas
#---------------------------------------------------------
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Por favor, inicia sesión.", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return decorated_function
#---------------------------------------------------------

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        fecha_str = request.form["fecha"]

        # Asignar el rol "Cliente" por defecto
        rol_id = 2

        # Validamos
        if not username or not password or not email:
            flash("Por favor, completa los campos obligatorios.", "danger")
            return redirect(url_for("auth.register"))

        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            flash("La fecha no tiene un formato válido.", "danger")
            return redirect(url_for("auth.register"))

        # Verificar si el usuario 
        if Usuario.query.filter_by(username=username).first():
            flash("El usuario ya existe. Elige otro nombre de usuario.", "danger")
            return redirect(url_for("auth.register"))

        # Crear usuario con contraseña hasheada y guardar
        nuevo_usuario = Usuario(
            username=username,
            password=generate_password_hash(password),  # Hashear la contraseña
            nombre=nombre,
            apellido=apellido,
            email=email,
            telefono=telefono,
            fecha=fecha,
            rol_id=rol_id
        )
        nuevo_usuario.save()
        flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        usuario = Usuario.query.filter_by(username=username).first()

        if usuario and check_password_hash(usuario.password, password):
            session["user_id"] = usuario.id
            session["username"] = usuario.username
              # Redirigimos según el rol del usuario
            if usuario.rol_id == 1:  #  1 corresponde a "Admin"
                flash(f"Bienvenido, {usuario.username}.", "success")
                return redirect(url_for("admin.dashboard"))  # Página CRUD
            else:  # Cliente
                flash(f"Bienvenido, {usuario.username}.", "success")
                return redirect(url_for("home.index"))  # Página Catálogo

        flash("Credenciales incorrectas. Intenta de nuevo.", "danger")
    return render_template("auth/login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()  # Limpia la sesión
    flash("Has cerrado sesión correctamente.", "success")
    return redirect(url_for('home.index'))
