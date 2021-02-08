from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date
from app.helpers import permisos
from app.models.configuracion import Configuracion
from app.models.rol import Rol

def centros():
    permisos.validar_permisos('')
    return render_template('centros.html')


def login():
    if request.method == 'POST':    
        params  = request.form
        usuario = User.get_by_email_and_pass(params['usuario'], params['clave'])
        user    = User.get_by_username(params['usuario'])
        if user.activo == 0:
            return render_template('errores/usuario_deshabilitado.html')
        if usuario:
            mensaje = "Se logueo correctamente"
            session['usuario'] = usuario
            permisos.validar_permisos('')
            configuracion = Configuracion.get_config()
            return render_template('index.html', mensaje=mensaje, configuracion=configuracion)
        else:
            mensaje = "No logro autenticarse, vuelva a intentarlo."
            return render_template('/auth/login.html', mensaje=mensaje)
    return render_template('/auth/login.html')

def logout():
    session.clear()
    return redirect(url_for('index'))

def edit_usuario(id):
    permisos.validar_permisos('user_edit')
    usuario = User.get_by_id(id)
    roles   = Rol.query.all()
    if request.method == 'POST':
        u = request.form
        mensaje = ''
        if User.existe_usuario(u['usuario']) and not u['usuario'] == usuario.usuario:
            mensaje="El nombre de usuario ya existe"
        elif User.existe_email(u['email']) and not u['email'] == usuario.email:
            mensaje="El email ya existe"
        else:
            nuevos_roles = request.form.getlist("roles")
            User.edit(id, u['usuario'], u['clave'], u['nombre'], u['apellido'], u['email'], u['activo'], nuevos_roles)
            mensaje = "Usuario creado exitosamente"
            usuarios = User.all()
            #return render_template('usuario/editar_usuario.html', mensaje=mensaje, usuario=usuario)
            return redirect(url_for('index_usuario', mensaje=mensaje, usuarios=usuarios))
        return render_template('usuario/editar_usuario.html', usuario=usuario, mensaje_error=mensaje, roles=roles)
    else:
        return render_template('usuario/editar_usuario.html', usuario=usuario, roles=roles)

def activar(id):
    permisos.validar_permisos('user_edit')
    User.activar_user(id)
    return redirect(url_for('index_usuario'))

def desactivar(id):
    permisos.validar_permisos('user_edit')
    User.desactivar_user(id)
    return redirect(url_for('index_usuario'))

def index_usuario(nombre=' ',estado='todos',page=1):
    permisos.validar_permisos('user_show')
    per_page = Configuracion.get_config().cantPagina
    usuario = User.all()
    if request.method == 'GET':
        nombre = nombre
        estado = estado
    if request.method == 'POST':
        page=1
        params = request.form
        nombre = params['nombre'] or ' '
        estado = params['estado']
    usuario = User.query.filter_by(historico=0)
    if nombre != ' ':
        usuario = usuario.filter(User.nombre.like('%' + nombre + '%'))
    if estado != 'todos':
        usuario = usuario.filter_by(activo = estado)
    usuario = usuario.paginate(page, per_page=per_page)

    return render_template('usuario/index_usuario.html', usuario=usuario, nombre = nombre, estado = estado)

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
            return redirect(url_for('index_usuario', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito))
        return render_template('usuario/crear_usuario.html', mensaje_error= mensaje_error, mensaje_exito=mensaje_exito)
    else:
        return render_template('usuario/crear_usuario.html')

def borrar(id):
    permisos.validar_permisos('user_delete')
    mensaje= "Se borro el usuario"
    User.delete(id)
    return redirect(url_for('index_usuario'))


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