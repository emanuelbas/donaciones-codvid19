from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date
from app.helpers import permisos, api_requests
from app.models.configuracion import Configuracion
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro
from requests import get

# https://sodocumentation.net/flask/topic/6460/pagination

def go_index(nombre=' ',estado='todos',page=1):
	permisos.validar_permisos('centro_index')
	todos_los_estados = Estado_centro.all()
	per_page = Configuracion.get_config().cantPagina

	if request.method == 'GET':
		nombre = nombre
		estado = estado

	if request.method == 'POST':
		page=1
		params = request.form
		nombre = params['nombre'] or ' '
		estado = params['estado']

	if estado == 'todos':
		lista = Centro_de_ayuda.query.filter_by(historico=0).filter(Centro_de_ayuda.nombre.like('%'+nombre+'%'))
	else:
		lista = Centro_de_ayuda.query.filter_by(historico=0).filter(Centro_de_ayuda.nombre.like('%'+nombre+'%')).filter_by(estado_id = estado)

	obtener_municipios(lista)
	lista = lista.paginate(page, per_page=per_page)

	return render_template('centro_de_ayuda/index_centros.html', lista_de_centros=lista, nombre=nombre, estado=estado, estados = todos_los_estados)

def crear_centro():
	mensaje_error = ''
	mensaje_exito = ''
	if request.method == "POST":
		form = request.form
		if Centro_de_ayuda.existe_nombre(form['municipio'],form['nombre']):
			print(form.getlist("tipos"))
			mensaje_error="Ya existe un centro con ese nombre para el municipio indicado"
			return render_template('centro_de_ayuda/crear_centro.html', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)
		else:
			print("Voy a intentar crear el centro")
			print(form)
			Centro_de_ayuda.hola_mundo()		
			res = Centro_de_ayuda.crear(nombre=form['nombre'],direccion=form['direccion'],telefono=form['telefono'],hapertura=form['hora_apertura'],hcierre=form['hora_cierre'],email=form['email'],sitio_web=form['web'],corx=form['corx'],cory=form['cory'],lista_de_tipos=form.getlist("tipos"),id_municipio=form['municipio'],id_estado=1,protocolo='PDF',historico=0)
			print("Bien, no se rompio")	
			if res:
				mensaje_exito = "Centro creado exitosamente"
			else:
				mensaje_error = "Hubo algun problema"
			return render_template('centro_de_ayuda/crear_centro.html', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)
	else:
		lista_de_municipios = obtener_dic_de_municipios()
		lista_de_tipos = Tipo_de_centro.all()
		return render_template('centro_de_ayuda/crear_centro.html', tipos= lista_de_tipos, municipios=lista_de_municipios, mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)


def obtener_municipios(lista):
	dic_de_municipios = api_requests.dictionaryOfMunicipios()
	for centro in lista:
		centro.municipio.nombre = dic_de_municipios['data']['Town'][str(centro.municipio.id)]['name']

def obtener_dic_de_municipios():
	''' Obtiene un diccionario municipios desde una API, separados por IDs '''
	return api_requests.dictionaryOfMunicipios()['data']['Town']
