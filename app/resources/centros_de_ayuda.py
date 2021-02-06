from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date
from app.helpers import permisos, api_requests
from app.models.configuracion import Configuracion
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro
from requests import get
from werkzeug import secure_filename
import datetime

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

	lista = Centro_de_ayuda.query.filter_by(historico=0)
	if estado != 'todos':
		lista = lista.filter_by(estado_id = estado)
	if nombre != ' ':
		lista = lista.filter(Centro_de_ayuda.nombre.like('%'+nombre+'%'))

	obtener_municipios(lista)
	lista = lista.paginate(page, per_page=per_page)

	return render_template('centro_de_ayuda/index_centros.html', lista_de_centros=lista, nombre=nombre, estado=estado, estados = todos_los_estados)

def crear_centro():
	permisos.validar_permisos('centro_create')
	mensaje_error = ''
	mensaje_exito = ''
	if request.method == "POST":
		form = request.form
		l_tipos = form.getlist("tipos")
		if len(l_tipos) == 0:
			mensaje_error= "Debe ingresar algún tipo de Centro"
			return render_template('centro_de_ayuda/crear_centro.html', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)

		h_ini = form["hora_apertura"]
		h_fin = form["hora_cierre"]
	
		if not horas_validas(h_ini, h_fin):
			mensaje_error= "La hora de apertura debe ser menor que la hora de cierre"
			return render_template('centro_de_ayuda/crear_centro.html', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)

		if not '@' in form['email']:
			mensaje_error= "El email debe contener '@'"
			return render_template('centro_de_ayuda/crear_centro.html', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito) 
			
		if Centro_de_ayuda.existe_nombre(form['municipio'],form['nombre']):
			print(form.getlist("tipos"))
			mensaje_error="Ya existe un centro con ese nombre para el municipio indicado"
			return render_template('centro_de_ayuda/crear_centro.html', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)
		else:
			res = Centro_de_ayuda.crear(
				nombre=form['nombre'],
				direccion=form['direccion'],
				telefono=form['telefono'],
				hapertura=form['hora_apertura'],
				hcierre=form['hora_cierre'],
				email=form['email'],
				sitio_web=form['web'],
				corx=str(form['corx']),
				cory=str(form['cory']),
				lista_de_tipos=l_tipos,
				id_municipio=form['municipio'],
				id_estado=1,
				protocolo='PDF',
				historico=0)
			# Teniendo la id del nuevo centro puedo guardar su archivo
			file     = request.files['pdf']
			path     = 'app/static/uploads/'
			filename = str(res.id)+'_' + "Protocolo_de_visita.pdf"
			file.save(path+filename)
			Centro_de_ayuda.set_protocolo(id=res.id,fn=filename)

			if res:
				mensaje_exito = "Centro creado exitosamente"
				return redirect(url_for('centros', mensaje_exito=mensaje_exito))
			else:
				mensaje_error = "Hubo algun problema"
				return render_template('centro_de_ayuda/crear_centro.html', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)
	else:
		lista_de_municipios = obtener_dic_de_municipios()
		lista_de_tipos      = Tipo_de_centro.all()
		return render_template('centro_de_ayuda/crear_centro.html', tipos= lista_de_tipos, municipios=lista_de_municipios, mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)

def editar_centro(id):
	permisos.validar_permisos('centro_edit')
	mensaje_error = ''
	mensaje_exito = ''

	#Obtener el centro a editar
	centro = Centro_de_ayuda.query.get(id)

	#Formateo los horarios
	print(centro.hora_de_apertura.hour)
	h1 = datetime.time(centro.hora_de_apertura.hour,centro.hora_de_apertura.minute)
	h2 = datetime.time(centro.hora_de_apertura.hour,centro.hora_de_apertura.minute)
	formated_hora_de_apertura = h1
	formated_hora_de_cierre = h2

	lista_de_tipos = Tipo_de_centro.all()
	lista_de_municipios = obtener_dic_de_municipios()
	if request.method == "GET":
			
		return render_template('centro_de_ayuda/editar_centro.html',
			centro=centro,
			tipos= lista_de_tipos,
			municipios=lista_de_municipios,
			mensaje_error= mensaje_error,
			mensaje_exito=mensaje_exito)
	else:
		form = request.form
		l_tipos = form.getlist("tipos")
		if len(l_tipos) == 0:
			mensaje_error= "Debe ingresar algún tipo de Centro"
			return render_template('centro_de_ayuda/editar_centro.html',
			centro=centro,
			tipos= lista_de_tipos,
			municipios=lista_de_municipios,
			mensaje_error= mensaje_error,
			mensaje_exito=mensaje_exito)

		h_ini= form["hora_apertura"]
		h_fin = form["hora_cierre"]
		
		if not horas_validas(h_ini, h_fin):
			mensaje_error= "La hora de apertura debe ser menor que la hora de cierre"
			return render_template('centro_de_ayuda/editar_centro.html',
			centro=centro,
			tipos= lista_de_tipos,
			municipios=lista_de_municipios,
			mensaje_error= mensaje_error,
			mensaje_exito=mensaje_exito)

		if not '@' in form['email']:
			mensaje_error= "El email debe contener '@'"
			return render_template('centro_de_ayuda/editar_centro.html',
			centro=centro,
			tipos= lista_de_tipos,
			municipios=lista_de_municipios,
			mensaje_error= mensaje_error,
			mensaje_exito=mensaje_exito)

		print("Hora de apertura quedo en: "+form['hora_apertura'])
		res = Centro_de_ayuda.editar(id=id,
			nombre=form['nombre'],
			direccion=form['direccion'],
			telefono=form['telefono'],
			hapertura=form['hora_apertura'],
			hcierre=form['hora_cierre'],
			email=form['email'],
			sitio_web=form['web'],
			corx=str(form['corx']),
			cory=str(form['cory']),
			lista_de_tipos=l_tipos,
			id_municipio=form['municipio'],
			id_estado=1,
			protocolo='PDF',
			historico=0)

		if res:
			mensaje_exito = "Centro editado exitosamente"
		else:
			mensaje_error = "Hubo algun problema"
		lista_de_municipios = obtener_dic_de_municipios()
		lista_de_tipos      = Tipo_de_centro.all()
		return render_template('centro_de_ayuda/editar_centro.html',
			centro=centro,
			tipos= lista_de_tipos,
			municipios=lista_de_municipios,
			mensaje_error= mensaje_error,
			mensaje_exito=mensaje_exito)

def horas_validas(h_ini, h_fin):
	h_ini     = h_ini.split(":")
	ini_horas = int(h_ini[0])
	ini_mins  = int(h_ini[1])
	h_fin     = h_fin.split(":")
	fin_horas = int(h_fin[0])
	fin_mins  = int(h_fin[1])
	if ini_horas < fin_horas:
		return True
	else:
		if ini_horas == fin_horas and ini_mins < fin_mins:
			return True
		else:
			return False
	return False 


def mostrar_centro(id):
	permisos.validar_permisos('centro_show')
	centro           = Centro_de_ayuda.query.get(id)
	nombre_municipio = api_requests.name_of_town(centro.municipio_id)
	return render_template('centro_de_ayuda/mostrar_centro.html', centro=centro, municipio=nombre_municipio)


def obtener_municipios(lista):
	dic_de_municipios = api_requests.dictionaryOfMunicipios()
	for centro in lista:
		centro.municipio.nombre = dic_de_municipios['data']['Town'][str(centro.municipio.id)]['name']

def obtener_dic_de_municipios():
	''' Obtiene un diccionario municipios desde una API, separados por IDs '''
	return api_requests.dictionaryOfMunicipios()['data']['Town']


def borrar_centro(id):
	permisos.validar_permisos('centro_delete')
	Centro_de_ayuda.borrar(id)
	return redirect(url_for('centros'))

def aprobar_centro(id):
	permisos.validar_permisos('centro_edit')
	Centro_de_ayuda.aprobar(id)
	return redirect(url_for('centros'))

def rechazar_centro(id):
	permisos.validar_permisos('centro_edit')
	Centro_de_ayuda.rechazar(id)
	return redirect(url_for('centros'))

def publicar_centro(id):
	permisos.validar_permisos('centro_edit')
	Centro_de_ayuda.publicar(id)
	return redirect(url_for('centros'))

def despublicar_centro(id):
	permisos.validar_permisos('centro_edit')
	Centro_de_ayuda.despublicar(id)
	return redirect(url_for('centros'))