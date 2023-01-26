from src.dominio.entidad.proyecto import Proyecto
from src.dominio.entidad.usuario import Usuario

class UsuarioServicio():

    @classmethod
    def mostrarProyectosPorUsuario(self, usuario, proyectos):
        usuario = usuario.to_JSON()
        usuario['proyectos'] = []

        for proyecto in proyectos:
            usuario['proyectos'].append(proyecto.to_JSON())

        return usuario