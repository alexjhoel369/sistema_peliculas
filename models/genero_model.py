from database import db

class Genero(db.Model):
    __tablename__ = "generos"

    id = db.Column(db.Integer, primary_key=True)
    genero = db.Column(db.String(80), nullable=False)
    
    # Relación con la tabla Usuario
    peliculas = db.relationship('Pelicula', back_populates='genero')

    def __init__(self, genero):
        self.genero = genero  
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Genero.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Genero.query.get(id)
    
    def update(self, genero=None):
        if genero:
            self.genero = genero
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
