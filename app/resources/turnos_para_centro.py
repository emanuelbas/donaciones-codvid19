from flask import render_template, abort, url_for, request, redirect, session, flash, jsonify
from datetime import date
from app.models.turnos_para_centro import Turno
from app.models.centro_de_ayuda import Centro_de_ayuda
from app.models.turnos_para_cada_centro import Turnos_para_cada_centro
from app.models.configuracion import Configuracion
from app.helpers import permisos
import time
import datetime


def index_turno(id='', page=1, email=' '):
    permisos.validar_permisos('turno_index')
    per_page = Configuracion.get_config().cantPagina
    
    
    centros = Centro_de_ayuda.all()
    if request.method == 'GET':
        email = email
    if request.method == 'POST':
        page = 1
        params = request.form
        email = params['email'] or ' '
    if email ==' ':
        if id:
           
           turnos_todos = Turno.get_proximos_turnos(id).filter(Turno.email.like('%'+'%')).paginate(page, per_page=per_page)
           return render_template('turnos_para_centro/index_turno.html', turnos=turnos_todos, centros=centros, email=email, id=id)
        else:
           turnos_todos = Turno.query.filter(Turno.email.like('%'+'%')).paginate(page, per_page=per_page)
           return render_template('turnos_para_centro/index_turno.html', turnos=turnos_todos, centros=centros, email=email)
    else:
        if id:
            turnos_todos = Turno.query.filter_by(centro_id=id).filter(Turno.email.like('%'+email+'%')).paginate(page, per_page=per_page)
            return render_template('turnos_para_centro/index_turno.html', turnos=turnos_todos, centros=centros, email=email, id=id)
        else:
            turnos_todos = Turno.query.filter(Turno.email.like('%'+email+'%')).paginate(page, per_page=per_page)
            return render_template('turnos_para_centro/index_turno.html', turnos=turnos_todos, centros=centros, email=email)

    # if request.method == 'POST':
    #   c = request.form
    #  turnos = Turno.select_turno(c['centro'])
    # return render_template('turnos_para_centro/index_turno.html', turnos=turnos, centros=centros)
    # else:
    #   return render_template('turnos_para_centro/index_turno.html', turnos=turnos_todos, centros=centros)


def crear_turno(id_centro):
    permisos.validar_permisos('turno_create')
    centros     = Centro_de_ayuda.all()
    turnos_todos= Turno.all()
    centro      = Centro_de_ayuda.query.filter_by(id=id_centro).first()
    if request.method == 'POST':
        t         = request.form
        fecha     = t['fecha']
        id_centro = t['id_centro']
        solo_fecha= t['solo_fecha']

        if solo_fecha == "si":
            # Leer los turnos ocupados
            #fecha = fecha.strftime("%Y-%m-%d")
            turnos_ocupados = Turno.query.filter_by(centro_id=id_centro).filter_by(dia=fecha).all()

            # Generar lista de horarios disponibles
            turnos_disponibles = ["09:00 - 09:30","09:30 - 10:00", "10:00 - 10:30", "10:30 - 11:00",
            "11:00 - 11:30", "11:30 - 12:00", "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30",
            "13:30 - 14:00", "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30", "15:30 - 16:00"]
            for turno_ocupado in turnos_ocupados:
                # Armar fecha_ocupada
                # Quitar de turnos_disponibles
                
            # Enviar a un template
            return render_template('turnos_para_centro/crear_turno_con_fecha.html', centro=id_centro, fecha=fecha, turnos=turnos_disponibles)

        # Teniendo todos los datos solo queda hacer el alta como antes
        # 06 February 2021 (Saturday) - Quito esto para la modificacion de turnos
        #h_i = t['hora_ini']
        #h_f = t['hora_fin']
        #hora_ini = datetime.datetime.strptime(h_i, "%H:%M")
        #hora_fin = datetime.datetime.strptime(h_f, "%H:%M")

        #print(hora_ini.hour, ':', hora_ini.minute)
        #if str(t['dia']) < str(date.today()):
        #    mensaje = "La fecha ya paso, no puede crear los turnos"
        #    hora_ini = t['hora_ini']
        #    hora_fin = t['hora_fin']
        #    dia = t['dia']
        #    return render_template('turnos_para_centro/crear_turno.html', mensaje=mensaje, centro= centro, centros=centros, h_ini=hora_ini, h_fin=hora_fin, dia=dia)
        #while hora_ini != hora_fin:
        #    var1 = hora_ini
        #    var1 = str(var1.hour)+':'+str(var1.minute)
        #    var = hora_ini + datetime.timedelta(minutes=30)
        #    var = str(var.hour)+':'+str(var.minute)
        #    Turno.create(var1, var, t['dia'], t['centro'])
        #    hora_ini = hora_ini + datetime.timedelta(minutes=30)
        #return redirect(url_for('index_turno', id=id_centro, turnos=turnos_todos))

    else:

        return render_template('turnos_para_centro/crear_turno.html', centro= centro, centros=centros)

def crear_turno_para_fecha():
    permisos.validar_permisos('turno_create')
    form  = request.form
    centro= form['id_centro']
    fecha = form['fecha']
    print("Ok se esta abriendo el segundo template")
    return render_template('turnos_para_centro/crear_turno_para_fecha.html', centro=centro, fecha=fecha)

def editar_turno(id):
    permisos.validar_permisos('turno_edit')
    turno = Turno.get_by_id(id)
    if request.method == 'POST':
        t = request.form
        if t['email'] == '':
            disponible = 1
        else:
            disponible = 0
        Turno.edit(id, t['email'], t['telefono'], disponible)
        return redirect(url_for('index_turno', turno=turno))
    else:
        return render_template('turnos_para_centro/editar_turno.html', turno=turno)


def sacar_turno(id):
    permisos.validar_permisos('turno_edit')
    turno = Turno.get_by_id(id)
    if request.method == 'POST':
        t = request.form
        if t['email'] == '':
            disponible = 1
        else:
            disponible = 0
        Turno.edit(id, t['email'], t['telefono'], disponible)
        return redirect(url_for('index_turno', turno=turno))
    else:
        return render_template('turnos_para_centro/sacar_turno.html', turno=turno)


def borrar_turno(id):
    permisos.validar_permisos('turno_delete')
    Turno.delete(id)
    turno = Turno.all()
    return redirect(url_for('index_turno', turno=turno))


def horas_validas(h_ini, h_fin):
    h_ini    = h_ini.split(":")
    ini_horas= int(h_ini[0])
    ini_mins = int(h_ini[1])
    h_fin    = h_fin.split(":")
    fin_horas= int(h_fin[0])
    fin_mins = int(h_fin[1])
    if ini_horas < fin_horas:
        if ini_mins < fin_mins:
            return True
    return False        