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

# agregado para el login


def backend():
    params = request.form
    usuario = User.get_by_email_and_pass(params['usuario'], params['clave'])
    # print(usuario)
    if usuario:
        mensaje = "se logueo correctamente"
        session['usuario'] = request.form['usuario']
        print(session['usuario'])
        return render_template('backend.html', mensaje=mensaje)
    else:
        mensaje = "el usuario no pudo loguearse porque no existe"
        return render_template('/auth/login.html', mensaje=mensaje)
        # return redirect( url_for('index'))


def logout():
    session.clear()
    return redirect(url_for('index'))


def edit_usuario(id):
    usuario = User.get_by_id(id)
    if request.method == 'POST':
        u = request.form
        User.edit(id, u['usuario'], u['clave'], u['nombre'], u['apellido'], u['email'], u['activo'])
        mensaje = "Se modifico el usuario correctamente"
        return render_template('usuario/editar_usuario.html', usuario=usuario, mensaje=mensaje)
        #return redirect(url_for('edit_usuario', usuario=usuario, mensaje=mensaje))
    else:
        return render_template('usuario/editar_usuario.html', usuario=usuario)
        #return redirect(url_for('edit_usuario', usuario=usuario))


def index_usuario():
    usuario = User.all()
    return render_template('usuario/index_usuario.html', usuario=usuario)

def new_usuario():

    if request.method == 'POST':
        u = request.form
        User.new(u['usuario'], u['clave'], u['nombre'], u['apellido'], u['email'], u['activo'])
        mensaje = " Se agrego el usuario correctamente"
        return render_template('usuario/new_usuario.html', mensaje=mensaje)
    else:
        return render_template('usuario/new_usuario.html')

def delete_usuario(id):
    usuario = User.all()
    User.delete(id)
    #return render_template('usuario/index_usuario.html', usuario=usuario)
    return redirect(url_for('index_usuario', usuario=usuario))