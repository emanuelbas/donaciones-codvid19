from flask import render_template, abort, url_for, request, redirect, session, flash, jsonify
from datetime import date
from app.db import db
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
    f = str(date.today())
    if request.method == 'POST':
        t         = request.form
        fecha     = t['fecha']
        id_centro = t['id_centro']
        solo_fecha= t['solo_fecha']

        if solo_fecha == "si":
            turnos_ocupados = Turno.query.filter_by(centro_id=id_centro).filter_by(dia=fecha).filter_by(disponible=0).filter_by(borrado=0).all()

            turnos_disponibles = ["09:00 - 09:30","09:30 - 10:00", "10:00 - 10:30", "10:30 - 11:00",
            "11:00 - 11:30", "11:30 - 12:00", "12:00 - 12:30", "12:30 - 13:00", "13:00 - 13:30",
            "13:30 - 14:00", "14:00 - 14:30", "14:30 - 15:00", "15:00 - 15:30", "15:30 - 16:00"]
            for turno_ocupado in turnos_ocupados:
                # Armar fecha_ocupada - Tuve que cambiar hora_ini y hora_fin a VARCHAR en la BD
                fecha_ocupada = turno_ocupado.hora_ini+" - "+turno_ocupado.hora_fin
                try:
                    turnos_disponibles.remove(fecha_ocupada)
                except:
                    pass
            return render_template('turnos_para_centro/crear_turno_con_fecha.html', centro=id_centro, fecha=fecha, turnos=turnos_disponibles)

        hora_ini    = t['bloque_horario'][0:5]
        hora_fin    = t['bloque_horario'][8:13]
        email       = t['email']
        telefono    = t['telefono']
        fecha       = t['fecha']
        nombre      = t['nombre']
        apellido    = t['apellido']
        borrado     = 0
        disponible  = 0
        nuevo_turno = Turno(email=email, telefono=telefono, hora_ini=hora_ini, hora_fin=hora_fin,
                            dia=fecha, borrado=borrado, centro_id=id_centro, disponible=disponible, nombre=nombre, apellido=apellido)
        db.session.add(nuevo_turno)
        db.session.commit()

        return redirect(url_for('index_turno', id=id_centro, turnos=turnos_todos))

    else:

        return render_template('turnos_para_centro/crear_turno.html', centro= centro, centros=centros, f=f)

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
        return redirect(url_for('index_turno', id=turno.centro_id ,turno=turno))
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
    id_centro = Turno.query.filter_by(id=id).first().centro_id
    Turno.delete(id)
    turno = Turno.all()
    return redirect(url_for('index_turno', id=id_centro))


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