from app.models.configuracion import Configuracion
# Estoy probando unas cosas, si no sirve lo borro! 

def titulo():
	return Configuracion.get_config()['titulo']
def email():
	return Configuracion.get_config()['mail']
def descripcion():
	return Configuracion.get_config()['descripcion']
def hojas_por_pagina():
	return Configuracion.get_config()['cantPagina']