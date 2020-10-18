from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date


def quienesomos():
    usuario = User.all()
    return render_template('quienesomos.html', usuario=usuario)


def centros():
    return render_template('centros.html')


def login():
    return render_template('/auth/login.html')

# agregado para el login

# A tener en cuenta!
# When the session data is stored in the server you can be sure that any 
# data that you write to it is as secure as your server.
def backend():
    params = request.form
    usuario = User.get_by_email_and_pass(params['usuario'], params['clave'])
    if usuario:
        mensaje = "se logueo correctamente"
        session['usuario'] = usuario
        print(session['usuario'])
        return render_template('backend.html', mensaje=mensaje)
    else:
        mensaje = "el usuario no pudo loguearse porque no existe"
        return render_template('/auth/login.html', mensaje=mensaje)
        # return redirect( url_for('index'))


def logout():
    session.clear()
    return redirect(url_for('index'))


def editarUsuario(id):
    usuario = User.get_by_id(id)
    if request.method == 'POST':
        u = request.form
        User.edit(id, u['usuario'], u['clave'], u['nombre'], u['apellido'], u['email'], u['activo'])
        mensaje = "Se modifico el usuario correctamente"
        return render_template('usuario/editar_usuario.html', usuario=usuario, mensaje=mensaje)
    else:
        return render_template('usuario/editar_usuario.html', usuario=usuario)


def index_usuario():
    usuario = User.all()
    return render_template('usuario/index_usuario.html', usuario=usuario)

def crear_usuario():
    if request.method == 'POST':
        u = request.form
        User.create(u['usuario'], u['clave'], u['nombre'], u['apellido'], u['email'])
        mensaje = "Usuario creado exitosamente"
        return render_template('usuario/crear_usuario.html', mensaje=mensaje)
    else:
        return render_template('usuario/crear_usuario.html')