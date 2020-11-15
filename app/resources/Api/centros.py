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
	return jsonify(response), 202





def get_list_of_tipos(centro):
	tipos = []
	for tipo in centro.tipos_de_centro:
		tipos.append({'id':tipo.id, 'nombre':tipo.nombre})
	return tipos