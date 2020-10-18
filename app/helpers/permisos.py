from flask import session, abort
from app.helpers.auth import authenticated
from app.models.configuracion import Config
from app.models.usuario import User


def validar_permisos(un_permiso):
	if sitio_cerrado() and no_es_admin():
		abort(503)

	# Si el usuario no tiene una cookie de sesion válida muestro un mensaje de error
	if not authenticated(session):
		abort(401)
	
	if no_tiene_el_permiso_solicitado(un_permiso):
		abort(401)
	return


########   Funciones auxiliares   ########

def no_es_admin():
	return not User.tiene_rol(session["usuario"], 'admin')

def sitio_cerrado():
	return not Config.habilitado()

def no_tiene_el_permiso_solicitado(un_permiso):
	return False
	#return not User.tiene_permiso(session["usuario"], un_permiso)