from flask import Blueprint
from src.util.utils import response
from src.infraestructura.repositorio.proyecto import ProyectoRepositorio
from src.dominio.servicio.proyecto import ProyectoServicio

class ProyectoAplicacion():
    base = Blueprint('proyecto', __name__)

    def __init__(self):
        self.base.add_url_rule('/', view_func=self.listarProyectos, methods=["GET"])
        self.base.add_url_rule('/tiempo', view_func=self.listarProyectosTiempo, methods=["GET"])

    def listarProyectos(self):
        try:
            proyectos = ProyectoRepositorio.obtenerProyectos()
            return response(True, proyectos)
        except Exception as ex:
            return response(False, str(ex), 500)

    def listarProyectosTiempo(self):
        try:
            proyectos = ProyectoRepositorio.obtenerProyectos()
            proyectosDiasPorTerminar = ProyectoServicio.mostrarTiempoRestanteProyectos(proyectos)
            return response(True, proyectosDiasPorTerminar)
        except Exception as ex:
            return response(False, str(ex), 500)