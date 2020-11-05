from flask import Flask
from flask import jsonify
from flask import request
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro


def devolverCentros():
	#centros = {
	#"id": "1",
	#"nombre": "centro1",
	#"descripcion": esto es una prueba
	#}
	centros = centro_de_ayuda.all()
	print(centros)
	#print(request.json)
	return jsonify(centros) 
