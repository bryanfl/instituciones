CREATE DATABASE name_db;

-- Table: public.institucion
-- Insertar estos por el servicio web
{
    "nombre": "Agencia de Calidad de la Educación",
    "descripcion": "Trabajamos con las comunidades educativas evaluando, orientando e informando para lograr una educación integral de calidad que permita que en Chile todas y todos puedan crecer y desarrollarse superando las brechas.", 
    "fechaCreacion": "11/08/2011"
}

{
    "nombre": "Agencia e Sustentabilidad y Cambio Climático",
    "descripcion": "Somos un Comité de la Corporación de Fomento de la Producción (CORFO) y tenemos como misión fomentar la inclusión de la dimensión del cambio climático y el desarrollo sostenible en el sector privado y en los territorios.", 
    "fechaCreacion": "01/01/1998"
}

{
    "nombre": "Autoridad Sanitaria",
    "descripcion": "La autoridad regional debe fiscalizar y sancionar disposiciones del Código Sanitario y otras normativas. Asimismo, la Seremi de Salud fiscaliza materias como higiene y seguridad del ambiente y de los lugares de trabajo; alimentos; laboratorios; farmacias; inhumaciones; exhumaciones y traslado de cadáveres.", 
    "fechaCreacion": "14/10/1924"
}

{
    "nombre": "Corporación de Asistencia Judicial Región Metropolitana",
    "descripcion": "Somos un Comité de la Corporación de Fomento de la Producción (CORFO) y tenemos como misión fomentar la inclusión de la dimensión del cambio climático y el desarrollo sostenible en el sector privado y en los territorios.", 
    "fechaCreacion": "01/01/1998"
}

-- Estos datos si puede registrar en la base de datos defrente ya que no hay un servicio para crear registro en estas tablas

-- Table: public.usuario

INSERT INTO public.usuario(
id, nombre, apellidos, "RUT", "fechaNacimiento", cargo, edad)
VALUES (1, 'Bryan', 'Fernandez Lizana', '75283977', '9/9/1999', 'Desarrolador Backend Python', 23);

INSERT INTO public.usuario(
id, nombre, apellidos, "RUT", "fechaNacimiento", cargo, edad)
VALUES (2, 'Jose', 'Romero Alvarado', '61233427', '30/1/1998', 'Desarrolador FrontEnd', 24);

-- Table: public.proyecto

INSERT INTO public.proyecto(
id, nombre, descripcion, "fechaInicio", "fechaFin", "idInstitucion", "idUsuario")
VALUES (1, 'Proyecto de Apoyo Estudiantil', 'Se realizara apoyo al estudiante mediante asesorias en una pagina web', '1/1/2023', '1/2/2023', 1, 1);

INSERT INTO public.proyecto(
id, nombre, descripcion, "fechaInicio", "fechaFin", "idInstitucion", "idUsuario")
VALUES (2, 'Proyecto de Gestion de calidad', 'Se realizara un proyecto de encuesta estudiantil con metricas', '2/2/2023', '1/4/2023', 1, 1);

INSERT INTO public.proyecto(
id, nombre, descripcion, "fechaInicio", "fechaFin", "idInstitucion", "idUsuario")
VALUES (3, 'Proyecto de Monitoreo Climatico', 'Se realizara un dashboard para el monitoreo de los cambios climaticos', '1/1/2023', '1/2/2023', 2, 2);

INSERT INTO public.proyecto(
id, nombre, descripcion, "fechaInicio", "fechaFin", "idInstitucion", "idUsuario")
VALUES (4, 'Proyecto de Control Sanitario', 'Se realizara un proyecto web para la gestion de Sanidad en el pais', '5/2/2023', '5/3/2023', 3, 2);

INSERT INTO public.proyecto(
id, nombre, descripcion, "fechaInicio", "fechaFin", "idInstitucion", "idUsuario")
VALUES (5, 'Proyecto de Asistencia Judicial', 'Se realizara una gestion de de las Asistencias Judiciales en el area metropolitana', '10/4/2023', '1/5/2023', 4, 1);
