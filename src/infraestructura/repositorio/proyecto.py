from flask import Blueprint
from src.dominio.entidad.proyecto import Proyecto
from src.dominio.entidad.usuario import Usuario
from init import db

class ProyectoRepositorio():

    @classmethod
    def obtenerProyectos(self):
        try:
            proyectos = db.session.query(Proyecto).all()
            proyectosJSON = [proyecto.to_JSON() for proyecto in proyectos]
            return proyectosJSON
        except Exception as ex:
            raise Exception(ex)