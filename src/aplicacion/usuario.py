from flask import Blueprint
from src.util.utils import response
from src.infraestructura.repositorio.usuario import UsuarioRepositorio
from src.dominio.servicio.usuario import UsuarioServicio

class UsuarioAplicacion():
    base = Blueprint('usuario', __name__)

    def __init__(self):
        self.base.add_url_rule('/', view_func=self.listarUsuarios, methods=["GET"])
        self.base.add_url_rule('/<rut>', view_func=self.listarUsuarioPorRut, methods=["GET"])

    def listarUsuarios(self):
        try:
            usuarios = UsuarioRepositorio.obtenerUsuarios()
            return response(True, usuarios)
        except Exception as ex:
            return response(False, str(ex), 500)

    def listarUsuarioPorRut(self, rut):
        try:
            usuario, proyectos = UsuarioRepositorio.obtenerProyectosPorUsuarioPorRUT(rut)

            if usuario is None:
                return response(True, 'Usuario no encontrado', 404)

            usuario = UsuarioServicio.mostrarProyectosPorUsuario(usuario, proyectos)
            return response("OK", usuario)
        except Exception as ex:
            return response(False, str(ex), 500)
