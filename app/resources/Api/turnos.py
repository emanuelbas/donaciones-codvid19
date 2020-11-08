from flask import Flask
from flask import jsonify
from flask import request
from app.models.turnos_para_centro import Turno
from app.models.centro_de_ayuda import Centro_de_ayuda
from datetime import date, time

# terminar las apis, hay que hacer otro def para cuando no tengo fecha


def turnos_disponibles_con_fecha(fecha):
    #centros = Centro_de_ayuda.all()

    turnos = Turno.all()
    lista = []
    for turno in turnos:
        if turno.disponible == 1:
            if str(turno.dia) == fecha:
                dic = {'fecha': str(turno.dia),
                       'hora_fin': turno.hora_fin,
                       'hora_inicio': turno.hora_ini,
                       'centro_id': turno.centro_id
                       }
                lista.append(dic)
    response = {'Turnos': lista, 'Error': '500 Internal Server Error'}
    return jsonify(response)


def turnos_disponibles_sin_fecha():
    turnos = Turno.all()
    lista = []
    for turno in turnos:
        if turno.disponible == 1:
            if str(turno.dia) == str(date.today()):
                dic = {'fecha': str(turno.dia),
                       'hora_fin': turno.hora_fin,
                       'hora_inicio': turno.hora_ini,
                       'centro_id': turno.centro_id
                       }
                lista.append(dic)
    response = {'Turnos': lista, 'Error': '500 Internal Server Error'}
    return jsonify(response)


def reserva():
    reserva = "hola reserva"
    return reserva
