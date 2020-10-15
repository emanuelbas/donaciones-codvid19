from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date


def quienesomos():
    usuario = User.all()
    print(usuario)
    return render_template('quienesomos.html', usuario=usuario)

def centros():
    return render_template('centros.html')

def login():
    return render_template('/auth/login.html')

#agregado para el login
def backend():
	params=request.form
	usuario = User.get_by_email_and_pass(params['usuario'], params['clave'])
	#print(usuario)
	if usuario:
		mensaje = "se logueo correctamente"
		session['usuario'] = request.form['usuario']		
		return render_template('backend.html',mensaje=mensaje)
	else: 
		mensaje = "el usuario no pudo loguearse porque no existe"
		return render_template('/auth/login.html', mensaje=mensaje)
		#return redirect( url_for('index')) 
def logout():
    session.clear()
    return redirect(url_for('index'))