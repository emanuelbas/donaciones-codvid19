from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date
from app.helpers import permisos
from app.models.configuracion import Configuracion
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro

# Estaba viendo esto cuando me cai dormido https://sodocumentation.net/flask/topic/6460/pagination
def get_index(page=1):
    permisos.validar_permisos('centro_index')
    per_page = Configuracion.get_config().cantPagina
    lista = Centro_de_ayuda.query.filter_by(historico=0).paginate(page, per_page=per_page)
    print("Se levanto esta lista:")
    print(lista)
    return render_template('centro_de_ayuda/index_centros.html', lista_de_centros=lista)


def filtrar_centros(page=1):
	permisos.validar_permisos('centro_index')
	per_page = Configuracion.get_config().cantPagina
	params = request.form
	nombre = params['nombre'] or ''
	nombre = '%'+nombre+'%'
	estado = params['estado']
	if estado == 'todos':
		lista = Centro_de_ayuda.query.filter(Centro_de_ayuda.nombre.like(nombre)).paginate(page, per_page=per_page)
	else:
		lista = Centro_de_ayuda.query.filter(Centro_de_ayuda.nombre.like(nombre)).filter_by(estado = estado).paginate(page, per_page=per_page)
	
	print("Se levanto esta lista:")
	print(lista)
	return render_template('centro_de_ayuda/index_centros.html', lista_de_centros=lista)