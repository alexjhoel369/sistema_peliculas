from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String(255), nullable=False)
    apellido = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)  # Corregido

    # Relación con la tabla Rol
    rol = db.relationship('Rol', back_populates='usuarios')
    ventas = db.relationship('Venta', back_populates='usuario')

    def __init__(self, username, password, nombre, apellido, email, telefono, fecha, rol_id):
        self.username = username
        self.password = self.hash_password(password)
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.fecha = fecha
        self.rol_id = rol_id
    
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    
    def update(self, username=None, password=None, nombre=None, apellido=None, email=None, telefono=None, fecha=None, rol_id=None):
        if username:
            self.username = username
        if password:
            self.password = self.hash_password(password)
        if nombre:
            self.nombre = nombre    
        if apellido:
            self.apellido = apellido
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono
        if fecha:
            self.fecha = fecha    
        if rol_id:
            self.rol_id = rol_id 
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
