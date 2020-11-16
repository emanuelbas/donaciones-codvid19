from flask import Flask
from flask import jsonify
from flask import request 
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro

def mostrarCentros(page=1):
	centros = Centro_de_ayuda.all()
	lista = []
	for centro in centros:
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
	response = {'centros':lista, 'total':len(centros), 'pagina':page }
	return jsonify(response)

def cargarCentros():
	#crear centro
	#pasarlo al diccionario
	#armar la respuesta
	if request.method == "GET" :
		response = { "nombre" : "centro1" , 
		 "direccion" : "Calle 23",
		 "telefono" : "9111233255",
         "hora_de_apertura" : "09:00",
         "hora_de_cierre" : "10:00",
         "tipos" : [],
         "sitio_web" : "http://www.centrodeprueba.gov",
         "email" : "contacto@centrodeprueba.gov",
		 "id_municipio" : "1" 
        }
		return jsonify(response)
	datos = request.get_json()
	nombre = datos["nombre"]
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

	return jsonify(response)