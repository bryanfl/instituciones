from init import db

class Institucion(db.Model):
    __tablename__ = 'institucion'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    descripcion = db.Column(db.String(), nullable=False)
    fechaCreacion = db.Column(db.Date, nullable=False)

    def __init__(self, nombre, descripcion, fechaCreacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaCreacion = fechaCreacion

    def __repr__(self):
        return f"<Institucion {self.nombre}>"

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'fechaCreacion': str(self.fechaCreacion)
        }