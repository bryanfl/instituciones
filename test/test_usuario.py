import pytest
from src.infraestructura.repositorio.usuario import UsuarioRepositorio
from src.dominio.servicio.usuario import UsuarioServicio
from src.dominio.entidad.usuario import Usuario
from init import app

def test_existen_usarios_registradas():
    with app.app_context():
        usuarios = UsuarioRepositorio.obtenerUsuarios()
        assert len(usuarios) > 0

@pytest.mark.parametrize(
    "rut, cantidadProyectos",
    [
        ("75283977", 3),
        ("61233427", 2)
    ]
)
def test_obtener_proyectos_por_usuario(rut, cantidadProyectos):
    with app.app_context():
        usuario, proyectos = UsuarioRepositorio.obtenerProyectosPorUsuarioPorRUT(rut)
        usuario = UsuarioServicio.mostrarProyectosPorUsuario(usuario, proyectos)

        assert len(usuario['proyectos']) == cantidadProyectos