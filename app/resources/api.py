from flask import Flask
from flask import jsonify
from flask import request 
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro

def mostrarCentros():
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
	response = {'centros':lista, 'total':1, 'pagina':1 }
	return jsonify(response)