from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date
from app.helpers import permisos
from app.models.configuracion import Configuracion
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro

# https://sodocumentation.net/flask/topic/6460/pagination
def get_index( page=1):
    permisos.validar_permisos('centro_index')
    per_page = Configuracion.get_config().cantPagina
    lista = Centro_de_ayuda.query.filter_by(historico=0).paginate(page, per_page=per_page)
    todos_los_estados = Estado_centro.all()
    return render_template('centro_de_ayuda/index_centros.html', lista_de_centros=lista, estados=todos_los_estados)


def filtrar_centros(page=1):
	permisos.validar_permisos('centro_index')
	todos_los_estados = Estado_centro.all()
	per_page = Configuracion.get_config().cantPagina

	nombre = ''
	estado = 'todos'
	if request.method == 'POST':
		params = request.form
		nombre = params['nombre'] or ''
		estado = params['estado']

	if estado == 'todos':
		lista = Centro_de_ayuda.query.filter_by(historico=0).filter(Centro_de_ayuda.nombre.like('%'+nombre+'%')).paginate(page, per_page=per_page)
	else:
		lista = Centro_de_ayuda.query.filter_by(historico=0).filter(Centro_de_ayuda.nombre.like('%'+nombre+'%')).filter_by(estado_id = estado).paginate(page, per_page=per_page)
	
	return render_template('centro_de_ayuda/index_centros.html', lista_de_centros=lista, estados=todos_los_estados, pasar_nombre=nombre, pasar_estado=estado)