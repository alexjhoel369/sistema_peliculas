from flask import Flask,request,redirect,url_for
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
from controllers import auth_controller
#-----------------------------------------------------

from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "miclavesecreta"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sistema_peliculas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
