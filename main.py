from flask import redirect, send_from_directory
from init import app
from src.aplicacion.institucion import InstitucionAplicacion
from src.aplicacion.proyecto import ProyectoAplicacion
from src.aplicacion.usuario import UsuarioAplicacion

app.register_blueprint(InstitucionAplicacion().base, url_prefix='/institucion')
app.register_blueprint(ProyectoAplicacion().base, url_prefix='/proyecto')
app.register_blueprint(UsuarioAplicacion().base, url_prefix='/usuario')

class Main:
    def __init__(self):
        app.add_url_rule('/', view_func= self.inicio, methods=['GET'])
        app.add_url_rule('/static/<path:path>', view_func=self.send_static, methods=['GET'])

    def inicio(self):
        return redirect("/swagger", code=302)

    def send_static(self, path):
        return send_from_directory('static', path)

Main()

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)

