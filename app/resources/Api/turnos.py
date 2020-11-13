from flask import Flask
from flask import jsonify
from flask import request
from app.models.turnos_para_centro import Turno
from app.models.centro_de_ayuda import Centro_de_ayuda
import time
import datetime

# terminar las apis, hay que hacer otro def para cuando no tengo fecha


def turnos_disponibles(id, fecha):
    #centros = Centro_de_ayuda.all()
    print("la fecha es:", str(fecha))
    turnos = Turno.select_turno(id)
    lista = []
    if fecha == 'fecha':
        fecha = str(date.today())
        print("ahora la fecha es:", fecha)

    for turno in turnos:
        if turno.disponible == 1:
            if str(turno.dia) == fecha:
                dic = {'centro_id': turno.centro_id,
                       'hora_inicio': turno.hora_ini,
                       'hora_fin': turno.hora_fin,
                       'fecha': str(turno.dia)
                       }
                lista.append(dic)
    response = {'Turnos': lista,
                'Error': 'No existe turno para la fecha seleccionada'}
    return jsonify(response)


def reserva(id):
    fecha = '2020-11-13'
    h_i = '11:00'
    hora_ini = datetime.datetime.strptime(h_i, "%I:%M") #mirar el %i por ahi no es el param correcto
    var1 = hora_ini
    var1 = str(var1.hour)+':'+str(var1.minute)
    var = hora_ini + datetime.timedelta(minutes=30)
    var = str(var.hour)+':'+str(var.minute)
    hora_fin = var
    turnos = Turno.query.filter_by(dia=fecha).all()

    lista = []
    ok = True

    for turno in turnos:

        if str(turno.centro_id) == str(id):
            dic = {'centro_id': turno.centro_id,
                   'hora_inicio': turno.hora_ini,
                   'hora_fin': turno.hora_fin,
                   'fecha': str(turno.dia)
                   }
            lista.append(dic)

    for l in lista:
        if l['hora_inicio'] == var1:
            ok = False
       
    if ok == True:
        Turno.create_reserva(var1, hora_fin, fecha, id)
        print("el turno se creo correctamente!!!!")
    else:
        print("EL TURNO NO SE CREO POR QUE YA EXISTE!!!!")    
    
    response = {'Turnos': lista,
                'Error': 'El turno que quiere reservar ya no esta disponible'}
    return jsonify(response)


# def turnos_disponibles(id):
 #   turnos = Turno.all()  # filtrar por fecha y si esta disponible
  #  lista = []             # la hora y la fecha no son modificables solo mostrarlas, generar todos los turnos de un dia vacios y irlos reservando
   # for turno in turnos:  # directamente filtrar los turnos disponibles y por fecha para no hacer esos 2 if
    #    if turno.disponible == 1:  # recibir el centro_id para buscar la fecha del turno por id centro , agregar el campo telefono
    #       if str(turno.dia) == str(date.today()):
    #          dic = {'fecha': str(turno.dia),
    #                'hora_fin': turno.hora_fin,
    #               'hora_inicio': turno.hora_ini,
    #              'centro_id': turno.centro_id
    #             }
    #      lista.append(dic)
    # response = {'Turnos': lista,
    #           'Error': 'No esxiste turno para la fecha seleccionada'}
    # return jsonify(response)
