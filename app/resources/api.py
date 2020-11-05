from flask import Flask
from flask import jsonify
from flask import request 
from app.models.centro_de_ayuda import Centro_de_ayuda, Municipio, Tipo_de_centro, Estado_centro
from flask_marshmallow import Marshmallow  #esto es nuevo

#init marshmallow
ma = Marshmallow(app)

#para realizar los abm 




def mostrarApi():
    return jsonify({'message': 'Bienvenido a la API'})
	
