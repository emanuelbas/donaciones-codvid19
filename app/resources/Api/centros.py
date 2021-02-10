from flask import Flask
from flask import jsonify
from flask import request 
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro
from app.models.turnos_para_centro import Turno
from flask import Response
from app.models.configuracion import Configuracion
import math
from datetime import datetime, timedelta

def mostrar_centros(page=1):

	try:
		per_page = Configuracion.get_config().cantPagina
		#Redondeo hacia arriba con ceil para obtener el total de paginas
		total = math.ceil(len(Centro_de_ayuda.query.filter_by(publicado=True).all())/per_page)
		centros = Centro_de_ayuda.query.filter_by(publicado=True).paginate(page, per_page=per_page).items
	except:
		return jsonify({"error":"500 Internal Server Error"}), 500
	
	lista = []
	for centro in centros:

	# Necesito jsonificarlo,
	# Como es un objeto de SQLAlchemy, no puedo jsonificarlo, tengo que pasarlo a diccionarios y listas
		lista_Tipos = []
		for tipo in centro.tipos_de_centro:
			lista_Tipos.append({'id':tipo.id, 'nombre':tipo.nombre})
		dic = {'nombre': centro.nombre, 'direccion': centro.direccion,
				'telefono': centro.telefono,'hora_apertura': str(centro.hora_de_apertura),
				'hora_cierre': str(centro.hora_de_cierre),
				'web': centro.sitio_web,'email': centro.email,
				'tipos': lista_Tipos
				}
		lista.append(dic)

	# Generar la respuesta con lo que piden en la actividad
	response = {'centros':lista, 'total':total, 'pagina':page }
	return jsonify(response), 200

def mostrar_centro(id):
	try:
		centro = Centro_de_ayuda.query.get(id)
	except:
		return jsonify({"error":"500 Internal Server Error"}), 500
	
	if not centro:
		return jsonify({"error":"404 Not Found"}), 404

	tipos = get_list_of_tipos(centro)
	dic = {"nombre":centro.nombre,
	"direccion":centro.direccion, "telefono":centro.telefono,
	"hora_apertura": str(centro.hora_de_apertura), "hora_cierre": str(centro.hora_de_apertura),
	"tipos": tipos, "web": centro.sitio_web, "email": centro.email}

	response = {'atributos':dic}
	return jsonify(response), 200





def get_list_of_tipos(centro):
	tipos = []
	for tipo in centro.tipos_de_centro:
		tipos.append({'id':tipo.id, 'nombre':tipo.nombre})
	return tipos

def cargarCentros():
	''' Controlador para el api Endpoint /api/crear_centro '''
	if request.method == "GET" :
		response = { "nombre" : "Nombre de Centro" , 
		 "direccion" : "La Plata, Calle 23 numero 123",
		 "telefono" : "9111233255",
         "hora_de_apertura" : "09:00",
         "hora_de_cierre" : "18:00",
         "tipos" : [3,2],
         "sitio_web" : "http://www.centrodeprueba.gov",
         "email" : "contacto@centrodeprueba.gov",
		 "id_municipio" : "1"
        }
		return jsonify(response)
	datos = request.get_json()
	
	# if !(datos["captcha"] = "ok") :
	# 	return jsonify({"error":"401 Error en el recaptcha"}), 401


	nombre = datos["nombre"]
	tipos = []
	for tipo in datos['tipos']:
		tipos.append({'id':tipo.id, 'nombre':tipo.nombre})
	res = Centro_de_ayuda.crear(
				nombre=datos['nombre'],
				direccion=datos['direccion'],
				telefono=datos['telefono'],
				hapertura=datos['hora_de_apertura'],
				hcierre=datos['hora_de_cierre'],
				email=datos['email'],
				sitio_web=datos['sitio_web'],
				corx=datos['latitud'],
				cory=datos['longitud'],
				lista_de_tipos=datos['tipos'],
				id_municipio=datos['id_municipio'],
				id_estado=1,
				protocolo='PDF',
				historico=0)
	response = {"atributos" : datos} 

	return jsonify(response),202


def mostrar_todos_centros():

	try:
		centros = Centro_de_ayuda.query.filter_by(publicado=True).all()
	except:
		return jsonify({"error":"500 Internal Server Error"}), 500
	
	lista = []
	for centro in centros:

	# Necesito jsonificarlo,
	# Como es un objeto de SQLAlchemy, no puedo jsonificarlo, tengo que pasarlo a diccionarios y listas
		lista_Tipos = []
		for tipo in centro.tipos_de_centro:
			lista_Tipos.append({'id':tipo.id, 'nombre':tipo.nombre})
		dic = {'nombre': centro.nombre, 'direccion': centro.direccion,
				'telefono': centro.telefono,'hora_apertura': str(centro.hora_de_apertura),
				'hora_cierre': str(centro.hora_de_cierre),
				'web': centro.sitio_web,'email': centro.email,
				'tipos': lista_Tipos,
				"lat" : centro.coordenada_x,
				"lng" : centro.coordenada_y,
				"id_municipio" : centro.municipio_id,
				"id_centro" : centro.id
				}
		lista.append(dic)

	# Generar la respuesta con lo que piden en la actividad
	response = {'centros':lista }
	return jsonify(response), 200


def centros_por_tipos():
	''' Controlador para el api Endpoint /api/estadisticas/tipos '''
	# Obtener los datos
	try:
		centros = Centro_de_ayuda.query.filter_by(publicado=True).all()
		tipos = Tipo_de_centro.query.all()
	except:
		return jsonify({"error":"500 Error en la lectura de la base de datos"}), 500

	contadores = {}
	for tipo in tipos:
		contadores[tipo.nombre] = 0

	# Procesarlos
	for centro in centros:
		for tipo_de_centro in centro.tipos_de_centro:
			contadores[tipo_de_centro.nombre] = contadores[tipo_de_centro.nombre] + 1

	
	# Generar respuesta
	res = []
	for tipo in tipos:
		res.append({"tipo" : tipo.nombre, "cantidad" : contadores[tipo.nombre]})


	response = {'centros_por_tipo':res}
	
	return jsonify(response), 200

def total_turnos_del_mes():
	''' Controlador para el api Endpoint /api/estadisticas/total_turnos_del_mes.
		Responde a un GET brindando los turnos solicitados en los últimos 30 días
	'''
	# Inicializar variables
	contadores_turnos_por_dia = {}
	dia_actual = datetime.now()
	for i in range(30):
		contadores_turnos_por_dia[dia_actual.strftime("%m-%d-%Y")] = 0	
		dia_actual = dia_actual - timedelta(days=1)
	# Leer tablas
	try:
		turnos = Turno.turnos_tomados_del_mes()
	except:
		return jsonify({"error":"500 Error en la lectura de la base de datos"}), 500

	# Procesar
	for turno in turnos:
		try:
			contadores_turnos_por_dia[turno.dia.strftime("%m-%d-%Y")] = contadores_turnos_por_dia[turno.dia.strftime("%m-%d-%Y")] + 1
		except:
			res = []
	# Generar respuesta
	res = []
	dia_actual = datetime.now()
	for i in range(30):
		str_del_dia = dia_actual.strftime("%m-%d-%Y")
		try:
			turnos_del_dia = contadores_turnos_por_dia[str_del_dia]
			res.append({"dia" : str_del_dia , "turnos" : turnos_del_dia})
		except:
			nada = 'nada'
		dia_actual = dia_actual - timedelta(days=1)

	response = {'turnos_por_dia': res}
	return jsonify(response), 200


def top10_centros_del_mes():
	''' Controlador para el api Endpoint /api/estadisticas/top10_centros_del_mes.
		Responde a un GET brindando los 10 con mayor cantidad de turnos y la cantidad de turnos
	'''
	# Leer tablas
	try:
		centros_y_sus_turnos = []
		todos_los_centros = Centro_de_ayuda.publicados()
		for centro in todos_los_centros:
			turnos_para_centro = Turno.turnos_tomados_para_centro(centro.id)
			cant_turnos = len(turnos_para_centro)
			centros_y_sus_turnos.append({"nombre" : centro.nombre , "cantidad" : cant_turnos})
	except:
		return jsonify({"error":"500 Error en la lectura de la base de datos"}), 500

	# Procesar
	centros_ordenados = sorted(centros_y_sus_turnos, key=lambda k: k['cantidad'], reverse=True) 
	mejores_10_centros = centros_ordenados[:10]
	mejores_10_centros.reverse()
	
	# Generar respuesta
	response = {'top_10': mejores_10_centros}
	return jsonify(response), 200