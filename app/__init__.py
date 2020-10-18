from os import path
from flask import Flask, url_for, render_template, g, request, session, flash, redirect
from app.models.usuario import User
from app.config import Config
from app.db import db
from flask_session import Session
from app.resources import user
from app.resources import config
#from flask_mysqldb import MySQL

def create_app():
	# Configuración inicial de la app
	app = Flask(__name__)
	app.config.from_object(Config)
	# session
	app.config['SESSION_TYPE'] = 'filesystem'
	Session(app)

	# config db
	app.secret_key = 'hola'
	app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://" + \
	    Config.DB_USER+":"+Config.DB_PASS+"@"+Config.DB_HOST+"/"+Config.DB_NAME
	db.init_app(app)


	# session agregado por maxi
	app.config['SESSION_TYPE'] = 'filesystem'
	Session(app)

	# Autenticacion agregado por maxi
	app.add_url_rule('/login', 'login', user.login)
	app.add_url_rule('/backend', 'user_backend', user.backend, methods=['POST'])
	app.add_url_rule('/logout', 'logout', user.logout)


	# ruta a quienes somos
	app.add_url_rule('/quienesomos', 'quienesomos',
	                 user.quienesomos, methods=["POST", "GET"])

	# ruta a centros
	app.add_url_rule('/centros', 'centros', user.centros, methods=["POST", "GET"])


	# ruta a login
	app.add_url_rule('/login', 'login', user.login)

	# CONFIGURACION
	app.add_url_rule('/configuracion/vista_configuracion', 'vista_configuracion',
	                 config.vista_configuracion, methods=["POST", "GET"])
	# usuario
	app.add_url_rule('/usuario/edit_usuario/<id>', 'edit_usuario', user.edit_usuario, methods=['POST', 'GET'])
	app.add_url_rule('/usuario/index_usuario', 'index_usuario', user.index_usuario, methods=["POST", "GET"])
	app.add_url_rule('/usuario/crear_usuario', 'crear_usuario', user.crear_usuario, methods=["POST", "GET"])
	app.add_url_rule("/usuarios/borrar_usuario/<id>", 'borrar_usuario', user.borrar, methods=['GET'])

	# ruta al backend
	app.add_url_rule('/backend', 'backend', user.backend, methods=["POST", "GET"])


	# index
	@app.route('/')
	def index():
	    return render_template('index.html')
	    
	return app