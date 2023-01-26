import pytest
from src.infraestructura.repositorio.proyecto import ProyectoRepositorio
from src.dominio.servicio.proyecto import ProyectoServicio
from init import app

def test_existen_proyectos_registradas():
    with app.app_context():
        proyectos = ProyectoRepositorio.obtenerProyectos()
        assert len(proyectos) > 0

def test_validar_dias_finalizacion():
    with app.app_context():
        proyectos = ProyectoRepositorio.obtenerProyectos()
        proyectosDiasPorTerminar = ProyectoServicio.mostrarTiempoRestanteProyectos(proyectos)
        validacion = True
        for proyecto in proyectosDiasPorTerminar:
            if not 'diasTermino' in proyecto:
                validacion = False

        assert validacion