from requests import get
from flask import json

# Devuelve un json con el municipio que corresponde a la id
def request_town(id):
	return False

def name_of_town(id):
	try:
		dic = get('https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios/'+str(id)).json()
		return dic['data']['Town'][str(id)]['name']
	except Exception as e:
		return 'API_ERROR'

def dictionaryOfMunicipios():
	try:
		return get('https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios?per_page=1000').json()
	except Exception as e:
		return 'API_ERROR'

#def actualizarDB():
#	try:
#		dic_of_towns = get('https://api-referencias.proyecto2020.linti.unlp.edu.ar/municipios?per_page=1000').json()['data']['Town']
#		sql = 'INSERT INTO `municipio` (`id`, `nombre`, `fase_id`) VALUES '
#		cont = 1
#		for town in dic_of_towns:
#
#			town[str(cont)]
#			sql = sql + "('"+la_id+"', '"+el_nombre+"', '"+la_fase+"'), "
#			cont = cont + 1
#
#
#	except Exception as e:
#		return False