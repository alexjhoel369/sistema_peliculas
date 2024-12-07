from database import db

class Venta(db.Model):
    __tablename__= "ventas"

    id = db.Column(db.Integer,primary_key = True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'),nullable=False)
    pelicula_id = db.Column(db.Integer, db.ForeignKey('peliculas.id'),nullable=False)
    fecha = db.Column(db.DateTime,nullable=False)

    # Relacion con la tabla Usuarios y Peluculas
    usuario = db.relationship('Usuario', back_populates='ventas')
    pelicula = db.relationship('Pelicula',back_populates='ventas')

    def __init__(self, usuario_id, pelicula_id, fecha ):
        self.usuario_id = usuario_id
        self.pelicula_id = pelicula_id
        self.fecha = fecha
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Venta.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Venta.query.get(id)
    
    def update (self, usuario_id=None,pelicula_id=None,fecha=None):
        if usuario_id and pelicula_id and fecha:
            self.usuario_id = usuario_id
            self.pelicula_id = pelicula_id
            self.fecha = fecha
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


