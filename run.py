from flask import Flask,request
import os
#----------------admin-------------------------------
from controllers import usuario_controller
from controllers import rol_controller
from controllers import genero_controller
from controllers import pelicula_controller
from controllers import venta_controller

#----------------principal----------------------------
from controllers import home_controller
from controllers import admin_controller
from controllers import client_controller
from controllers import auth_controller
#-----------------------------------------------------

from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "miclavesecreta"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sistema_peliculas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#------------------------------------------------------
# Configuración para subir imágenes
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#------------------------------------------------------
db.init_app(app)

#-----------------------------------------------------
app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(rol_controller.rol_bp)
app.register_blueprint(genero_controller.genero_bp)
app.register_blueprint(pelicula_controller.pelicula_bp)
app.register_blueprint(venta_controller.venta_bp)

#-----------------------------------------------------
app.register_blueprint(home_controller.home_bp)
app.register_blueprint(client_controller.client_bp)
app.register_blueprint(admin_controller.admin_bp)
app.register_blueprint(auth_controller.auth_bp)

#-----------------------------------------------------


@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path == path else ''
    return(dict(is_active = is_active))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)