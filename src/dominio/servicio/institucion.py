from src.dominio.entidad.institucion import Institucion
from src.dominio.entidad.proyecto import Proyecto
from src.dominio.entidad.usuario import Usuario

class InstitucionServicio():

    @classmethod
    def mostrarProyectosYUsuarioPorInstitucion(self, institucion, proyectosUsuario):
        institucion = institucion.to_JSON()
        institucion['proyectos'] = []

        for proyecto in proyectosUsuario:
            proyecto, usuario = proyecto

            institucion['proyectos'].append({
                "idProyecto": proyecto.id,
                "nombreProyecto": proyecto.nombre,
                "idUsuarioResponsable": usuario.id,
                "nombreUsuarioResponsable": usuario.nombre,
                "apellidosUsuarioResponsable": usuario.apellidos
            })

        return institucion

    @classmethod
    def mostrarInstitucionesConDireccion(self, instituciones):
        institucionesConDireccion = []
        url = 'https://www.google.com/maps/search/'

        for institucion in instituciones:
            institucion['direccion'] = url + institucion['nombre'][:3]
            institucionesConDireccion.append(institucion)

        return institucionesConDireccion

    @classmethod
    def validarCamposInstitucion(self, intitucion):
        if intitucion.nombre == "" or intitucion.descripcion == "" or intitucion.fechaCreacion == "":
            return False

        return True