from init import db

class Proyecto(db.Model):
    __tablename__ = 'proyecto'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    descripcion = db.Column(db.String())
    fechaInicio = db.Column(db.Date)
    fechaFin = db.Column(db.Date)
    idInstitucion = db.Column(db.Integer, db.ForeignKey("institucion.id"))
    idUsuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))

    def __init__(self, nombre, descripcion, fechaInicio, fechaFin, idInstitucion, idUsuario):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.idInstitucion = idInstitucion
        self.idUsuario = idUsuario

    def __repr__(self):
        return f"<Proyecto {self.nombre}>"

    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'fechaInicio': str(self.fechaInicio),
            'fechaFin': str(self.fechaFin),
            'idInstitucion': self.idInstitucion,
            'idUsuario': self.idUsuario,
        }