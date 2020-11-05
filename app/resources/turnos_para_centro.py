from flask import render_template, abort, url_for, request, redirect, session, flash, jsonify
from datetime import date
from app.models.turnos_para_centro import Turno
from app.models.centro_de_ayuda import Centro_de_ayuda
from app.models.turnos_para_cada_centro import Turnos_para_cada_centro


def index_turno():
    turnos_todos = Turno.all()
    centros = Centro_de_ayuda.all()

    if request.method == 'POST':
        c = request.form
        turnos = Turno.select_turno(c['centro'])
        return render_template('turnos_para_centro/index_turno.html', turnos=turnos, centros=centros)
    else:
        return render_template('turnos_para_centro/index_turno.html', turnos=turnos_todos, centros=centros)


def crear_turno():
    centros = Centro_de_ayuda.all()
    turnos_todos = Turno.all()
    if request.method == 'POST':
        t = request.form

        turnos = Turno.select_turno(t['centro'])

        for turno in turnos:

            if turno.bloque_turno == t['bloque_turno']:
                mensaje = "El turno en esa hora no esta disponible"
                return render_template('turnos_para_centro/crear_turno.html', centros=centros, mensaje=mensaje)

        Turno.create(t['email'], t['bloque_turno'],
                     t['dia'], t['centro'])
        return redirect(url_for('index_turno', turnos=turnos_todos))

    else:

        return render_template('turnos_para_centro/crear_turno.html', centros=centros)


def editar_turno(id):
    turno = Turno.get_by_id(id)
    print(turno.bloque_turno)
    if request.method == 'POST':
        t = request.form
        #if turno.bloque_turno == t['bloque_turno']:
         #       mensaje = "El turno en esa hora no esta disponible"
          #      return render_template('turnos_para_centro/crear_turno.html', mensaje=mensaje)
        Turno.edit(id, t['email'], t['bloque_turno'], t['dia'])
        return redirect(url_for('index_turno', turno=turno))
    else:
        return render_template('turnos_para_centro/editar_turno.html', turno=turno)


def borrar_turno(id):
    Turno.delete(id)
    turno = Turno.all()
    return redirect(url_for('index_turno', turno=turno))
