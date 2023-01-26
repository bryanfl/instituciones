from flask import Blueprint
from src.database.db import conectar_db
from src.dominio.entidad.institucion import Institucion
from src.dominio.entidad.proyecto import Proyecto
from src.dominio.entidad.usuario import Usuario
from init import db

class InstitucionRepositorio():

    @classmethod
    def obtenerInstituciones(self):
        try:
            institucionesQuery = Institucion.query.all()
            institucionesJSON = [institucion.to_JSON() for institucion in institucionesQuery]

            return institucionesJSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtenerInstitucionPorId(self, id):
        try:
            institucion = db.session.query(Institucion).get(id)

            return institucion
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtenerProyectosYUsuarioPorInstitucion(self, id):
        try:
            institucion = self.obtenerInstitucionPorId(id)
            proyectosUsuario = db.session.query(Proyecto, Usuario).filter(Proyecto.idUsuario == Usuario.id, Proyecto.idInstitucion == id).all()

            return institucion, proyectosUsuario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def registrarInstitucion(self, institucion):
        try:
            db.session.add(institucion)
            db.session.commit()
            return institucion
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def actualizarInstitucion(self, institucion, nuevosDatos):
        try:
            print(nuevosDatos)

            institucion.nombre = nuevosDatos['nombre']
            institucion.descripcion = nuevosDatos['descripcion']
            institucion.fechaCreacion = nuevosDatos['fechaCreacion']

            db.session.add(institucion)
            db.session.commit()

            return institucion
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def eliminarInstitucion(self, institucion):
        try:
            print(institucion)
            db.session.delete(institucion)
            db.session.commit()
        except Exception as ex:
            raise Exception(ex)