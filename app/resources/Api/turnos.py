from flask import Flask
from flask import jsonify
from flask import request
from app.models.turnos_para_centro import Turno
from app.models.centro_de_ayuda import Centro_de_ayuda
from datetime import time, date
import datetime

# terminar las apis, hay que hacer otro def para cuando no tengo fecha


def turnos_disponibles(id_centro, fecha):
    #centros = Centro_de_ayuda.all()
    print("la fecha es:", str(fecha))
    if fecha == 'fecha':
        fecha = str(date.today())
        print("ahora la fecha es:", fecha)
    turnos = Turno.query.filter_by(centro_id=id_centro).filter_by(
        dia=fecha).filter_by(disponible=1).all()
    print(turnos)

    if len(turnos) == 0:
        response = {'turnos': [],
                    'error': 'No existe turno para la fecha seleccionada'}
        return jsonify(response), 400

    lista = []

    for turno in turnos:
        dic = {'centro_id': turno.centro_id,
               'hora_inicio': str(turno.hora_ini),
               'hora_fin': str(turno.hora_fin),
               'fecha': str(turno.dia)
               }
        lista.append(dic)
    response = {'turnos': lista}
    return jsonify(response), 200


def reserva(id):
    ide = 892
    em = "reservado@gmail.com"
    te = "00000000000"
    fecha = '2020-11-15'
    h_i = '11:00:00'
    disponible = 0
    hora_ini = datetime.datetime.strptime(h_i, "%H:%M:%S")
    var1 = hora_ini
    var1 = str(var1.hour)+':'+str(var1.minute)+":"+str(var1.second)
    var = hora_ini + datetime.timedelta(minutes=30)
    var = str(var.hour)+':'+str(var.minute)+":"+str(var.second)
    hora_fin = var
    turnos = Turno.query.filter_by(dia=fecha).all()

    lista = []
    ok = True

    for turno in turnos:

        if str(turno.centro_id) == str(id):
            dic = {'centro_id': turno.centro_id,
                   'hora_inicio': str(turno.hora_ini),
                   'hora_fin': str(turno.hora_fin),
                   'fecha': str(turno.dia)
                   }
            lista.append(dic)

    for l in lista:
        if l['hora_inicio'] == var1:
            ok = False

    if ok == True:
        try:
            Turno.edit(ide, em, te, disponible)
            response = {'exito': 'Se agrego la reserva'}
            return jsonify(response)
        except:
            response = {'error': 'No existe el id del centro'}
            return jsonify(response)

    else:
        response = {'Turnos': lista,
                    'Error': 'El turno que quiere reservar ya no esta disponible'}
    return jsonify(response)


def pedir_reserva(centro_id):
    if request.method == "GET" :
        # Devuelvo el cuerpo de la consulta post
        response = {
            "email_donante" : "juan.perez@gmail.com",
            "telefono_donante": "2215930941",
            "hora_inicio": "15:00",
            "hora_fin": "18:00",
            "fecha": "2020-12-25"
        }
        return jsonify(response), 200
    else:
        # Me estan haciendo post!
        nuevo_turno = request.get_json()
        print(request.get_json())
        if Turno.es_valido(centro_id = nuevo_turno["centro_id"],
            fecha= nuevo_turno["fecha"],
            hora_inicio= nuevo_turno["hora_inicio"]):
            try:
                if Turno.reservar_turno(
                    centro_id = nuevo_turno["centro_id"],
                    email_donante = nuevo_turno["email_donante"],
                    telefono_donante = nuevo_turno["telefono_donante"],
                    hora_inicio = nuevo_turno["hora_inicio"],
                    hora_fin = nuevo_turno["hora_fin"],
                    fecha =  nuevo_turno["fecha"]
                    ):
                    diccionario = {
                        "centro_id": nuevo_turno["centro_id"],
                        "email_donante" : nuevo_turno["email_donante"],
                        "telefono_donante": nuevo_turno["telefono_donante"],
                        "hora_inicio": nuevo_turno["hora_inicio"],
                        "hora_fin": nuevo_turno["hora_fin"],
                        "fecha":  nuevo_turno["fecha"]
                        }
                    response = {"atributos": diccionario}
                    return jsonify(response), 200
            except Exception as e:
                return jsonify({"error":"500 Internal Server Error"}), 500
        else:
            return jsonify({"error":"400 Bad request"}), 400



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
