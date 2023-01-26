from init import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    apellidos = db.Column(db.String(), nullable=False)
    RUT = db.Column(db.String(8), nullable=False)
    fechaNacimiento = db.Column(db.Date)
    cargo = db.Column(db.String(), nullable=False)
    edad = db.Column(db.Integer, nullable=False)

    def __init__(self, nombre, apellidos, RUT, fechaNacimiento, cargo, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.RUT = RUT
        self.fechaNacimiento = fechaNacimiento
        self.cargo = cargo
        self.edad = edad

    def __repr__(self):
        return f"<Usuario {self.nombre}, {self.RUT}>"

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'RUT': self.RUT,
            'fechaNacimiento': str(self.fechaNacimiento),
            'cargo': self.cargo,
            'edad': self.edad,
        }