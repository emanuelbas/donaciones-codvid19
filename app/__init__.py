from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect
from app.models.usuario import User
from app.config import Config
from app.db import db
#from flask_mysqldb import MySQL

# Configuración inicial de la app
app = Flask(__name__)
app.config.from_object(Config)
# Carga de la configuración

# Server Side session

# Configure db
app.secret_key = 'hola'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + \
    Config.DB_USER+":"+Config.DB_PASS+"@"+Config.DB_HOST+"/"+Config.DB_NAME
db.init_app(app)

# Funciones que se exportan al contexto de Jinja2

# Autenticación

# Rutas de Consultas

# Rutas de Usuarios

# Ruta para el Home (usando decorator)


@app.route('/')
def home():
    return render_template('index.html')

# prueba maxi


@app.route('/quienesomos')
def quienesomos():
    usuario = User.all()
    print(usuario)
    return render_template('quienesomos.html', usuario=usuario)


@app.route('/centros')
def centros():
    return render_template('centros.html')


@app.route('/login')
def login():
    return render_template('/auth/login.html')
# prueba maxi

# Rutas de API-rest

# Handlers

# Retornar la instancia de app configurada
