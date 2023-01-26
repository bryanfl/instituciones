from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from decouple import config

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

def crearSwagger():
    swagger_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config= {
            'app-name': "API Kuantaz"
        }
    )

    return swagger_blueprint

def crearApp():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{config('USER')}:{config('PASSWORD')}@{config('HOST')}:{config('PORT')}/{config('DATABASE')}"
    CORS(app)

    app.register_blueprint(crearSwagger(), url_prefix=SWAGGER_URL)

    return app

def crearBaseDatos(app):
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    return db

app = crearApp()
db = crearBaseDatos(app)