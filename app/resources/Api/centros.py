from flask import Flask
from flask import jsonify
from flask import request 
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro
from flask import Response
from app.models.configuracion import Configuracion

def mostrarCentros(page=1):

	# Voy a mostrar el total de paginas, dado que es lo que le puede servir al frontend
	# para hacer los botones
	per_page = Configuracion.get_config().cantPagina
	total = len(Centro_de_ayuda.query.filter_by(publicado=True).all())/per_page
	

	# Recorro todos los centros publicados de la page actual
	centros = Centro_de_ayuda.query.filter_by(publicado=True).paginate(page, per_page=per_page).items
	if not centros:
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