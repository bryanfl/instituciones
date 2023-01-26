from flask import Blueprint
from src.dominio.entidad.usuario import Usuario
from src.dominio.entidad.proyecto import Proyecto
from init import db

class UsuarioRepositorio():

    @classmethod
    def obtenerUsuarios(self):
        try:
            usuarios = db.session.query(Usuario).all()
            usuariosJSON = [usuario.to_JSON() for usuario in usuarios]

            return usuariosJSON
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtenerProyectosPorUsuarioPorRUT(self, rut):
        try:
            usuario = db.session.query(Usuario).filter(Usuario.RUT == rut).first()

            if usuario is None:
                return usuario, []

            proyectos = db.session.query(Proyecto).filter(Proyecto.idUsuario == usuario.id).all()
            return usuario, proyectos
        except Exception as ex:
            raise Exception(ex)