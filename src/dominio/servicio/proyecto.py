from datetime import datetime, timedelta

class ProyectoServicio():

    @classmethod
    def mostrarTiempoRestanteProyectos(self, proyectos):
        proyectosConTiempo = []
        objFechaActual = datetime.now()

        for proyecto in proyectos:
            objFechaFin = datetime.strptime(str(proyecto["fechaFin"]), '%Y-%m-%d')
            tiempoRestante = objFechaFin - objFechaActual

            proyectosConTiempo.append({
                "nombre": proyecto["nombre"],
                "diasTermino": int(tiempoRestante/ timedelta(days=1))
            })
        return proyectosConTiempo