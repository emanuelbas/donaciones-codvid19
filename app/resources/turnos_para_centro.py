from flask import render_template, abort, url_for, request, redirect, session, flash, jsonify
from datetime import date
from app.models.turnos_para_centro import Turno
from app.models.centro_de_ayuda import Centro_de_ayuda
from app.models.turnos_para_cada_centro import Turnos_para_cada_centro
from app.models.configuracion import Configuracion
import time
import datetime


def index_turno(id='', page=1, email=' '):
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
           
           turnos_todos = Turno.query.filter_by(centro_id=id).filter(Turno.email.like('%'+'%')).paginate(page, per_page=per_page)
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


def crear_turno():
    centros = Centro_de_ayuda.all()
    turnos_todos = Turno.all()
    if request.method == 'POST':
        t = request.form
        h_i = t['hora_ini']
        h_f = t['hora_fin']
        hora_ini = datetime.datetime.strptime(h_i, "%I:%M")
        hora_fin = datetime.datetime.strptime(h_f, "%I:%M")

        print(hora_ini.hour, ':', hora_ini.minute)
        if str(t['dia']) < str(date.today()):
            mensaje = "La fecha ya paso, no puede crear los turnos"
            hora_ini = t['hora_ini']
            hora_fin = t['hora_fin']
            dia = t['dia']
            return render_template('turnos_para_centro/crear_turno.html', mensaje=mensaje, centros=centros, h_ini=hora_ini, h_fin=hora_fin, dia=dia)
        while hora_ini != hora_fin:
            var1 = hora_ini
            var1 = str(var1.hour)+':'+str(var1.minute)
            var = hora_ini + datetime.timedelta(minutes=30)
            var = str(var.hour)+':'+str(var.minute)
            Turno.create(var1, var, t['dia'], t['centro'])
            hora_ini = hora_ini + datetime.timedelta(minutes=30)
        return redirect(url_for('index_turno', turnos=turnos_todos))

    else:

        return render_template('turnos_para_centro/crear_turno.html', centros=centros)


def editar_turno(id):
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
    turno = Turno.get_by_id(id)
    if request.method == 'POST':
        t = request.form
        if t['email'] == '':
            disponible = 1
        else:
            disponible = 0
        Turno.edit(id, t['email'], turno.hora_ini,
                   turno.hora_fin, turno.dia, disponible)
        return redirect(url_for('index_turno', turno=turno))
    else:
        return render_template('turnos_para_centro/sacar_turno.html', turno=turno)


def borrar_turno(id):
    Turno.delete(id)
    turno = Turno.all()
    return redirect(url_for('index_turno', turno=turno))
