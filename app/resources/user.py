from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date
from app.helpers import permisos
from app.models.configuracion import Configuracion
def quienesomos():
    #configuracion = Configuracion.get_config() #esto hay que poner en algunos def para que cuando este desactivado el user no pueda entrar
    #if configuracion.activo == 0:
    #    return render_template('sitioDesactivado.html')
    permisos.validar_permisos('')
    usuario = User.all()
    print(usuario)
    return render_template('quienesomos.html', usuario=usuario)


def centros():
    permisos.validar_permisos('')
    #configuracion = Configuracion.get_config() #esto hay que poner en algunos def para que cuando este desactivado el user no pueda entrar
    #if configuracion.activo == 0:
    #    return render_template('sitioDesactivado.html')
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
    user = User.get_by_username(params['usuario'])
    #print(user.activo)
    if user.activo == 0:#preguntamos si el usuario esta desactivado
        return render_template('usuarioDesactivar.html')
    if usuario:
        mensaje = "Se logueo correctamente"
        session['usuario'] = usuario
        permisos.validar_permisos('')
        return render_template('backend.html', mensaje=mensaje)
    else:
        mensaje = "No logro autenticarse, vuelva a intentarlo."
        return render_template('/auth/login.html', mensaje=mensaje)

def logout():
    session.clear()
    return redirect(url_for('index'))


def edit_usuario(id):
    permisos.validar_permisos('user_edit')
    usuario = User.get_by_id(id)
    if request.method == 'POST':
        u = request.form
        mensaje = ''
        if User.existe_usuario(u['usuario']):
            mensaje="El nombre de usuario ya existe"
        elif User.existe_email(u['email']):
            mensaje="El email ya existe"
        else:
            User.edit(id, u['usuario'], u['clave'], u['nombre'], u['apellido'], u['email'], u['activo'])
            mensaje = "Usuario creado exitosamente"
            usuarios = User.all()
            #return render_template('usuario/editar_usuario.html', mensaje=mensaje, usuario=usuario)
            return redirect(url_for('index_usuario', mensaje=mensaje, usuarios=usuarios))
        return render_template('usuario/editar_usuario.html', usuario=usuario, mensaje_error=mensaje)
    else:
        return render_template('usuario/editar_usuario.html', usuario=usuario)

def activar(id):
    permisos.validar_permisos('user_edit')
    usuario = User.all()
    User.activar_user(id)
    return render_template('usuario/index_usuario.html', usuario=usuario)

def desactivar(id):
    permisos.validar_permisos('user_edit')
    usuario = User.all()
    User.desactivar_user(id)
    return render_template('usuario/index_usuario.html', usuario=usuario)

def index_usuario():
    permisos.validar_permisos('user_show')
    usuario = User.all()
    return render_template('usuario/index_usuario.html', usuario=usuario)

def crear_usuario():
    permisos.validar_permisos('user_create')
    if request.method == 'POST':
        u = request.form
        mensaje_error = ''
        mensaje_exito = ''
        if User.existe_usuario(u['usuario']):
            mensaje_error="El nombre de usuario ya existe"
        elif User.existe_email(u['email']):
            mensaje_error="El email ya existe"
        else:
            res = User.create(u['usuario'], u['clave'], u['nombre'], u['apellido'], u['email'])
            if res:
                mensaje_exito = "Usuario creado exitosamente"
            else:
                mensaje_error = "Hubo algun problema"
            lista_de_usuarios = User.all()
            return render_template('usuario/index_usuario.html', usuario = lista_de_usuarios, mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)
        return render_template('usuario/crear_usuario.html', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)
    else:
        return render_template('usuario/crear_usuario.html')

def borrar(id):
    permisos.validar_permisos('user_delete')
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
    permisos.validar_permisos('user_edit')
    User.agregar_rol(usuario,rol)
    lista_de_usuarios = User.all()
    return render_template('usuario/index_usuario.html', usuario = lista_de_usuarios)

