import os
from database import db
from werkzeug.utils import secure_filename

# Definiendo la ruta de las imágenes y las extenxiones
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Pelicula(db.Model):
    __tablename__ = "peliculas"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    año = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(120), nullable=False)
    idioma = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float(11, 2), nullable=False)
    imagen = db.Column(db.String(255), nullable=True) 
    genero_id = db.Column(db.Integer, db.ForeignKey('generos.id'), nullable=False)

    # Relación con la tabla Generos
    genero = db.relationship('Genero', back_populates='peliculas')
    ventas = db.relationship('Venta', back_populates='pelicula')

    def __init__(self, titulo, año, descripcion, idioma, precio, genero_id, imagen=None):
        self.titulo = titulo
        self.año = año
        self.descripcion = descripcion
        self.idioma = idioma
        self.precio = precio
        self.genero_id = genero_id
        self.imagen = imagen

    def save(self, file=None, upload_folder="static/uploads"):
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)
            self.imagen = filename  
            db.session.add(self)
            db.session.commit()

    @staticmethod
    def get_all():
        return Pelicula.query.all()

    @staticmethod
    def get_by_id(id):
        return Pelicula.query.get(id)

    def update(self, titulo=None, año=None, descripcion=None, idioma=None, precio=None, genero_id=None, file=None, upload_folder=UPLOAD_FOLDER):
        if titulo:
            self.titulo = titulo
        if año:
            self.año = año
        if descripcion:
            self.descripcion = descripcion
        if idioma:
            self.idioma = idioma
        if precio:
            self.precio = precio
        if genero_id:
            self.genero_id = genero_id
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(upload_folder, filename)
            file.save(filepath)
            self.imagen = filename

        db.session.commit()

    def delete(self):
        if self.imagen:
            imagen_path = os.path.join(UPLOAD_FOLDER, self.imagen)
            if os.path.exists(imagen_path):
                os.remove(imagen_path)  
        db.session.delete(self)
        db.session.commit()
