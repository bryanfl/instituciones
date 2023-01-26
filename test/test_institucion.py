import pytest
from src.infraestructura.repositorio.institucion import InstitucionRepositorio
from src.dominio.servicio.institucion import InstitucionServicio
from init import app

def test_existen_instituciones_registradas():
    with app.app_context():
        instituciones = InstitucionRepositorio.obtenerInstituciones()
        assert len(instituciones) > 0


@pytest.mark.parametrize(
    "idInstitucion, numeroProyectos",
    [
        (1, 2),
        (2, 1)
    ]
)
def test_validar_proyectos_por_institucion(idInstitucion, numeroProyectos):
    with app.app_context():
        institucion, proyectos = InstitucionRepositorio.obtenerProyectosYUsuarioPorInstitucion(idInstitucion)
        institucion = InstitucionServicio.mostrarProyectosYUsuarioPorInstitucion(institucion, proyectos)

        assert len(institucion['proyectos']) == numeroProyectos


def test_institucion_no_existe():
    with app.app_context():
        idInstitucion = 999
        institucion = InstitucionRepositorio.obtenerInstitucionPorId(idInstitucion)

        assert institucion is None

def test_validar_instituciones_con_direccion():
    with app.app_context():
        validacion = True

        instituciones = InstitucionRepositorio.obtenerInstituciones()
        institucionesConDireccion = InstitucionServicio.mostrarInstitucionesConDireccion(instituciones)

        for institucion in institucionesConDireccion:
            if not 'direccion' in institucion:
                validacion = False

        assert validacion
