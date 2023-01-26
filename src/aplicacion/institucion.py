from flask import Blueprint, request
from src.util.utils import response
from src.infraestructura.repositorio.institucion import InstitucionRepositorio
from src.dominio.servicio.institucion import InstitucionServicio
from src.dominio.entidad.institucion import Institucion

class InstitucionAplicacion():
    base = Blueprint('institucion', __name__)

    def __init__(self):
        self.base.add_url_rule('/', view_func=self.listarInstituciones, methods=["GET"])
        self.base.add_url_rule('/', view_func=self.registrarInstitucion, methods=["POST"])
        self.base.add_url_rule('/<id>', view_func=self.actualizarInstitucion, methods=["PUT"])
        self.base.add_url_rule('/<id>', view_func=self.eliminarInstitucion, methods=["DELETE"])
        self.base.add_url_rule('/<id>', view_func=self.listarInstitucionPorId, methods=["GET"])
        self.base.add_url_rule('/direcciones', view_func=self.listarInstitucionesConDireccion, methods=["GET"])

    @classmethod
    def listarInstituciones(self):
        try:
            instituciones = InstitucionRepositorio.obtenerInstituciones()
            return response(True, instituciones)
        except Exception as ex:
            return response(False, str(ex), 500)

    def listarInstitucionPorId(self, id):
        try:
            institucion, proyectos = InstitucionRepositorio.obtenerProyectosYUsuarioPorInstitucion(id)

            if institucion is None:
                return response(True, "La institucion indicada no esta registrada actualmente.", 404)

            institucion = InstitucionServicio.mostrarProyectosYUsuarioPorInstitucion(institucion, proyectos)
            return response(True, institucion)
        except Exception as ex:
            return response(False, str(ex), 500)

    def listarInstitucionesConDireccion(self):
        try:
            instituciones = InstitucionRepositorio.obtenerInstituciones()
            institucionesConDireccion = InstitucionServicio.mostrarInstitucionesConDireccion(instituciones)
            return response(True, institucionesConDireccion)
        except Exception as ex:
            return response(False, str(ex), 500)

    def registrarInstitucion(self):
        try:
            nombre = request.json['nombre']
            descripcion = request.json['descripcion']
            fechaCreacion = request.json['fechaCreacion']

            nuevaInstitucion = Institucion(nombre, descripcion, fechaCreacion)
            camposValidados = InstitucionServicio.validarCamposInstitucion(nuevaInstitucion)

            if not camposValidados:
                return response(False, "Debe ingresar todos los campos solicitados", 400)

            InstitucionRepositorio.registrarInstitucion(nuevaInstitucion)

            return response(True, nuevaInstitucion.to_JSON())

        except Exception as ex:
            return response(False, str(ex), 500)

    def actualizarInstitucion(self, id):
        try:
            institucion = InstitucionRepositorio.obtenerInstitucionPorId(id)

            if institucion is None:
                return response(True, "La institucion indicada no esta registrada actualmente.", 404)

            institucionActualizada = InstitucionRepositorio.actualizarInstitucion(institucion, request.json)

            return response(True, institucionActualizada.to_JSON())
        except Exception as ex:
            return response(False, str(ex), 500)

    def eliminarInstitucion(self, id):
        try:
            institucion, proyectos = InstitucionRepositorio.obtenerProyectosYUsuarioPorInstitucion(id)

            if institucion is None:
                return response(True, "La institucion indicada no esta registrada actualmente.", 404)

            if len(proyectos) > 0:
                return response(True, "No se puede eliminar la institucion porque tiene proyectos pendientes.", 200)

            InstitucionRepositorio.eliminarInstitucion(institucion)
            return response(True, f"Se elimino correctamente la institución con id {id}")

        except Exception as ex:
            return response(False, str(ex), 500)