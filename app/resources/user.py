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


# A tener en cuenta!
# When the session data is stored in the server you can be sure that any 
# data that you write to it is as secure as your server.
def backend():
    params = request.form
    usuario = User.get_by_email_and_pass(params['usuario'], params['clave'])
    if usuario:
        mensaje = "Se logueo correctamente"
        session['usuario'] = usuario
        print(session['usuario'])
        return render_template('backend.html', mensaje=mensaje)
    else:
        mensaje = "No logro autenticarse, vuelva a intentarlo."
        return render_template('/auth/login.html', mensaje=mensaje)

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

def crear_usuario():
    if request.method == 'POST':
        u = request.form
        User.create(u['usuario'], u['clave'], u['nombre'], u['apellido'], u['email'])
        mensaje = "Usuario creado exitosamente"
        lista_de_usuarios = User.all()
        return render_template('usuario/index_usuario.html', usuario = lista_de_usuarios)
    else:
        return render_template('usuario/crear_usuario.html')

def borrar(id):
    mensaje= "Se borro el usuario"
    User.delete(id)
    usuarios = User.all()
    return render_template('usuario/index_usuario.html', usuario=usuarios)

#funciones agregadas para el caso de activo/desactivo
def searchEstado(v):
    v = str(v)
    uss=[]
    if(v.lower() == 'activo'):
        uss = User.BySate(1)
    elif(v.lower() == 'bloqueado'):
        uss += User.BySate(0)
    return uss

def states():
    if not authenticated(session):
        abort(401)
    if not usuarioTienePermisoDe('usuario_index'):
        return render_template('vistasErrores/errorPermisos.html', permiso='usuario_index')
    v = User.change_status(request.args.get('email'), request.args.get('activo'))
    if(not v):
        flash("Hubo un error")

def agregar_rol(usuario,rol):
    User.agregar_rol(usuario,rol)
    lista_de_usuarios = User.all()
    return render_template('usuario/index_usuario.html', usuario = lista_de_usuarios)

