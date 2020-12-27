from app.db import db
from datetime import datetime
from sqlalchemy import update
from flask import session
from app.models.rol import Rol

# Siguiendo las diapo de la clase y este video https://www.youtube.com/watch?v=OvhoYbjtiKc
# Hay un trucazo para generar la BD en el minuto 11:37
roles = db.Table('usuario_tiene_rol',
                 db.Column('usuario_id', db.Integer, db.ForeignKey(
                     'usuario.id')),
                 db.Column('rol_id', db.Integer, db.ForeignKey(
                     'rol.id'))
                 )


class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    clave = db.Column(db.String)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    email = db.Column(db.String)
    activo = db.Column(db.Integer)
    fecha_actualizacion = db.Column(db.String)
    fecha_creacion = db.Column(db.String)
    historico = db.Column(db.Integer)

    # Voy a crear una relacion entre tablas
    # Lleva como argumento las clases involucradas
    roles = db.relationship('Rol', secondary=roles, backref=db.backref(
        'usuarios_con_el_rol', lazy=True), lazy='subquery')

    def all():
        return User.query.filter_by(historico=0).all()

    def get_by_username(u):
        return User.query.filter(User.usuario.contains(u)).first()

    def get_by_id(id):
        return User.query.get(id)

    def edit(i, us, cl, no, ap, em, ac, roles):
        lista_roles = []
        for rol in roles:
            lista_roles.append(Rol.query.filter_by(id = rol).first())
        datos = User.query.filter_by(id=i).first()
        datos.usuario = us
        datos.clave = cl
        datos.nombre = no
        datos.apellido = ap
        datos.email = em
        datos.activo = ac
        datos.roles = lista_roles
        db.session.commit()
        return datos

    # activar usuario
    def activar_user(ide):
        datos = User.query.filter_by(id=ide).first()
        datos.activo = 1
        db.session.commit()
        return datos

    # desactivar usuario
    def desactivar_user(ide):
        datos = User.query.filter_by(id=ide).first()
        datos.activo = 0
        db.session.commit()
        return datos

    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
    def create(us, cl, no, ap, em):
        today = datetime.now()
        nuevo_usuario = User(usuario=us, clave=cl, nombre=no, apellido=ap,
                             email=em, activo=True, fecha_actualizacion=today, fecha_creacion=today, historico=0)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return True

    def delete(idx):
        user = User.query.filter_by(id=idx).first()
        user.historico = 1
        db.session.commit()
        return True

    def get_by_email_and_pass(usuario, clave):
        return User.query.filter_by(usuario=usuario, clave=clave).first()

######################## VALIDACIONES ########################

    def existe_usuario(username):
        return User.query.filter_by(usuario=username).first()

    def existe_email(email):
        return User.query.filter_by(email=email).first()

######################## ROLES Y PERMISOS ########################

    def get_roles(id_usuario):
        return Usuario_tiene_rol.query.filter_by(usuario_id=id_usuario)

    def agregar_rol(usuario, rol):
        rol.usuarios.append(usuario)
        db.session.commit()
        return True

    def quitar_rol(usuario, rol):
        rol.usuarios.remove(usuario)
        db.session.commit()
        return True

    def tiene_rol(usuario, nombre_rol):
        res = False
        for rol in usuario.roles:
            if rol.nombre == nombre_rol:
                res = True
        return res

    def tiene_permiso(usuario, nombre_permiso):
        res = False
        for rol in usuario.roles:
            for permiso in rol.permisos:
                if permiso.nombre == nombre_permiso:
                    res = True
        return res

###################################################################