from flask import Flask
from flask import jsonify
from flask import request
from app.models.turnos_para_centro import Turno
from app.models.centro_de_ayuda import Centro_de_ayuda
from datetime import time, date
import datetime

# terminar las apis, hay que hacer otro def para cuando no tengo fecha


def turnos_disponibles(id_centro, fecha):
    ''' Devuelve una lista de bloques horarios disponibles para un centro y fecha determinados 

    USO: /api/centros/id_centro/<int:id_centro>/turnos_disponibles/fecha=<fecha>
    EJ : http://localhost:5000/api/centros/id_centro/1/turnos_disponibles/fecha=2021-02-08
    '''

    #centros = Centro_de_ayuda.all()

    # Obtener datos
    if fecha == 'fecha':
        fecha = str(date.today())
        print("ahora la fecha es:", fecha)
    turnos_ocupados = Turno.query.filter_by(centro_id=id_centro).filter_by(
        dia=fecha).filter_by(disponible=0).filter_by(borrado=0).all()


    # Procesar
    turnos_disponibles = ["09:00 - 09:30","09:30 - 10:00", "10:00 - 10:30", "10:30 - 11:00",
    "11:00 - 11:30", "11:30 - 12:00", "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30",
    "13:30 - 14:00", "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30", "15:30 - 16:00"]

    for turno_ocupado in turnos_ocupados:
        fecha_ocupada = turno_ocupado.hora_ini+" - "+turno_ocupado.hora_fin
        try:
            turnos_disponibles.remove(fecha_ocupada)
        except:
            pass

    if len(turnos_disponibles) == 0:
        response = {'turnos': [],
                    'error': 'No existe turno para la fecha seleccionada'}
        return jsonify(response), 400

    # Armar respuesta
    response = {'turnos': turnos_disponibles}
    return jsonify(response), 200


def reserva(id):
    ide = id
    em = "reservado@gmail.com"
    te = "00000000000"
    fecha = '2020-12-24'
    h_i = '08:00:00'
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


def pedir_reserva(id_centro):
    if request.method == "GET" :
        # Devuelvo el cuerpo de la consulta post
        response = {
            "centro_id":"8",
            "nombre":"Juan",
            "apellido":"Perez",
            "email_donante": "juan.perez@gmail.com",
            "fecha": "2020-11-12",
            "bloque_horario": "09:30 - 10:00",
            "telefono_donante": "2215930941"
        }
        return jsonify(response), 200
    else:
        # Me estan haciendo post!
        nuevo_turno = request.get_json()
        print("Se va a imprimir el json")
        print(request.get_json())

        # Obtengo los datos

        centro_id      = nuevo_turno["centro_id"]
        fecha          = nuevo_turno["fecha"]
        bloque_horario = nuevo_turno["bloque_horario"]
        hora_ini       = bloque_horario[0:5]
        hora_fin       = bloque_horario[8:13]
        email_donante  = nuevo_turno["email_donante"]
        telefono       = nuevo_turno["telefono_donante"]
        nombre         = nuevo_turno["nombre_donante"]
        apellido       = nuevo_turno["apellido_donante"]
        print("Se pudo leer bien el json")
        print(hora_ini)
        print(centro_id)
        print(fecha)
        # Proceso

        if Turno.es_valido(centro_id = centro_id,
            fecha= fecha,
            hora_inicio= hora_ini):
            try:
                if Turno.reservar_turno(
                    centro_id = centro_id,
                    email_donante = email_donante,
                    telefono_donante = telefono,
                    nombre_donante = nombre,
                    apellido_donante = apellido,
                    hora_inicio = hora_ini,
                    hora_fin = hora_fin,
                    fecha =  fecha
                    ):
                    diccionario = {
                        "centro_id": centro_id,
                        "email_donante" : email_donante,
                        "telefono_donante": telefono,
                        "nombre_donante" : nombre,
                        "apellido_donante" : apellido,
                        "hora_inicio": hora_ini,
                        "hora_fin": hora_fin,
                        "fecha":  fecha
                        }
                    response = {"atributos": diccionario}
                    return jsonify(response), 201
            except Exception as e:
                return jsonify({"error":"500 Internal Server Error"}), 500
        else:
            print("Sale porque le turno ya esta ocupado")
            return jsonify({"error":"400 Bad request"}), 400