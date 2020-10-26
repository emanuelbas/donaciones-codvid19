from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date
from app.helpers import permisos
from app.models.configuracion import Configuracion
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro


def get_index():
    permisos.validar_permisos('')
    lista = Centro_de_ayuda.all()
    print(lista[0])
    return render_template('centro_de_ayuda/index_centros.html', lista_de_centros=lista)


def filtrar_centros():
	permisos.validar_permisos('')
	params = request.form
	nombre = params['nombre'] or ''
	nombre = '%'+nombre+'%'
	estado = params['estado']
	if estado == 'todos':
		lista = Centro_de_ayuda.query.filter(Centro_de_ayuda.nombre.like(nombre))
	else:
		lista = Centro_de_ayuda.query.filter(Centro_de_ayuda.nombre.like(nombre)).filter_by(estado = estado)
	return render_template('centro_de_ayuda/index_centros.html', lista_de_centros=lista)