from flask import render_template, abort, url_for, request, redirect, session, flash
from datetime import date
from app.models.turnos_para_centro import Turno


def index_turno():
    turnos = Turno.all()
    return render_template('turnos_para_centro/index_turno.html', turnos=turnos)

def crear_turno():
    turno = Turno.all()
    if request.method == 'POST':
        
        t = request.form
        print(t)
        Turno.create(t['email'], t['bloque_turno'], t['dia'])
        return redirect(url_for('index_turno', turno=turno))
    else:
        return render_template('turnos_para_centro/crear_turno.html')
    
def editar_turno(id):
    turno = Turno.get_by_id(id)
    if request.method == 'POST':
        t = request.form
        Turno.edit(id, t['email'], t['bloque_turno'], t['dia'])
        return redirect(url_for('index_turno', turno=turno))
    else:
        print("NO entro")
        return render_template('turnos_para_centro/editar_turno.html', turno=turno)

    


def borrar_turno(id):
    Turno.delete(id)
    turno = Turno.all()
    return redirect(url_for('index_turno', turno=turno))