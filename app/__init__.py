from os import path, environ
from flask import Flask, render_template, g



def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Carga de la configuración
   
    # Server Side session
   
    # Configure db
    

    # Funciones que se exportan al contexto de Jinja2


    # Autenticación


    # Rutas de Consultas
   
    # Rutas de Usuarios
   
    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("index.html")

    # Rutas de API-rest
    
    # Handlers
   

    # Retornar la instancia de app configurada
    return app
