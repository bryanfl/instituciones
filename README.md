# instituciones
Esto es un ejemplo en un sistema operativo Windows

## Crear un entorno de desarrollo con Virtualenv
- Instalamos virtualenv
```sh
  pip install virtualenv
```

- Creamos nuestro entorno virtual
```sh
  virtualenv -p . venv
```

- Actiavamos el entorno virtual
```sh
  venv\Scripts\activate.bat
```

## Instalamos las librerias
Usaremos el archivo requirements.txt
```sh
  pip install -r requirements.txt
```

## Creamos las variables de entorno

Creamos un archivo .env (en la raíz del proyecto) para las variables de entorno y agregamos los datos requeridos:
```sh
HOST=host
PORT=port
USER=user
PASSWORD=password
DATABASE=database
```

## Iniciamos la base de datos Postgresql - SQLAchemy
- Primero crearemos la base de datos en Postgresql podemos hacerlo por comandos o con un gestor como lo seria `pgAdmin 4`
```sh
  CREATE DATABASE 'nombre_database'
```
- Definiremos el contexto de flask a nuestro archivo principal `main.py`
```sh
  set FLASK_APP=main.py
```
- Iniciamos la base de datos
```sh
  flask db init
```

- Preparamos la migracion
```sh
  flask db migrate
```

- Enviamos los cambios de la migracion a nuestra base de datos
```sh
  flask db upgrade
```

## Inciamos el proyecto
```sh
  flask run
```

Este sera levantado en el puerto `5000` y si ingresa a la URL `http://localhost:5000` lo enviara a la documentacion en `Swagger`

## Insertamos los datos de inicio
En el archivo `inserted_rows_db.sql` esta presente los datos que se registraran como inicio

- Datos de la institucion seran ingresados por el servicio `http://localhost:5000/institucion` method `POST`
- Datos de los usuarios y proyectos seran registrados por la base de datos, ya que no cuentan con un servicio para el registro


## Ejecutar las pruebas unitarias

Para ejecutar las pruebas unitarias solo basta con ejecutar el siguiente comando
```sh
  python -m pytest -v test\
```

## Tambien esta presente entre los documentos un archivo JSON que sirve para poder importar los servicios en postman
```sh
  Kuantaz.postman_collection.json
```
