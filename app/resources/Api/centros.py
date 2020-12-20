from flask import Flask
from flask import jsonify
from flask import request 
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro
from flask import Response
from app.models.configuracion import Configuracion
import math

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
	''' Controlador para el API Endpoint /Api/crear_centro '''
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
				corx="-38",
				cory="-58",
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
	''' Controlador para el API Endpoint /api/estadisticas/tipos '''
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
	''' Controlador para el API Endpoint /api/estadisticas/total_turnos_del_mes.
		Responde a un GET brindando los turnos solicitados en los últimos 30 días
	'''
	# Obtener los datos

	# Procesarlos

	# Generar respuesta
	response = {'turnos_por_dia':[
	{'dia' : '10-12-2020', 'turnos' : 25},
	{'dia' : '10-12-2020', 'turnos' : 5},
	{'dia' : '10-12-2020', 'turnos' : 3},
	{'dia' : '10-12-2020', 'turnos' : 43},
	{'dia' : '10-12-2020', 'turnos' : 234},
	{'dia' : '10-12-2020', 'turnos' : 234},
	{'dia' : '10-12-2020', 'turnos' : 4},
	{'dia' : '10-12-2020', 'turnos' : 3},
	{'dia' : '10-12-2020', 'turnos' : 233}
	]}
	return jsonify(response), 200


def top10_centros_del_mes():
	''' Controlador para el API Endpoint /api/estadisticas/top10_centros_del_mes.
		Responde a un GET brindando los 10 con mayor cantidad de turnos y la cantidad de turnos
	'''
	# Obtener los datos

	# Procesarlos

	# Generar respuesta
	response = {'top_10':[
	{'nombre' : 'Centro pepepito 1', 'cantidad' : 25},
	{'nombre' : 'Centro pepepito 2', 'cantidad' : 30},
	{'nombre' : 'Centro pepepito 3', 'cantidad' : 40},
	{'nombre' : 'Centro pepepito 4', 'cantidad' : 80},
	{'nombre' : 'Centro pepepito 5', 'cantidad' : 100},
	{'nombre' : 'Centro pepepito 6', 'cantidad' : 120},
	{'nombre' : 'Centro pepepito 7', 'cantidad' : 130},
	{'nombre' : 'Centro pepepito 8', 'cantidad' : 140},
	{'nombre' : 'Centro pepepito 9', 'cantidad' : 150},
	{'nombre' : 'Centro pepepito 10', 'cantidad' : 160},
	]}
	return jsonify(response), 200