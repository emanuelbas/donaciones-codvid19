from app.db import db
from datetime import datetime
from flask import session
from app.models.rol import Rol

# Siguiendo las diapo de la clase y este video https://www.youtube.com/watch?v=OvhoYbjtiKc
# Hay un trucazo para generar la BD en el minuto 11:37
roles = db.Table('usuario_tiene_rol',
    db.Column('usuario_id', db.Integer, db.ForeignKey('usuario.id'), primary_key=True),
    db.Column('rol_id', db.Integer, db.ForeignKey('rol.id'), primary_key=True)
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

    # Voy a crear una relacion entre tablas
    # Lleva como argumento las clases involucradas 
    roles = db.relationship('Rol', secondary=roles, backref=db.backref('usuarios_con_el_rol', lazy = True), lazy='subquery')

    def all():
        return User.query.all()

    def get_by_id(id):
        return User.query.get(id)

    def edit(i, us, cl, no, ap, em, ac):
        datos = User.query.filter_by(id=i).first()
        datos.usuario = us
        datos.clave = cl
        datos.nombre = no
        datos.apellido = ap
        datos.email = em
        datos.activo = ac
        db.session.commit()
        return datos


    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
    def create(us,cl,no,ap,em):
        today = datetime.now()
        nuevo_usuario = User(usuario = us, clave=cl, nombre = no, apellido=ap, email=em, activo= True, fecha_actualizacion= today, fecha_creacion = today)
        db.session.add (nuevo_usuario)
        db.session.commit()
        return True
    
    def delete(id):
        User.query.filter_by(id=id).delete()
        db.session.commit()
        return True 

    # COMPLETAR: Debe devolver True/False

    def tiene_rol(usuario, nombre_rol):
        return True

    # COMPLETAR: Debe devolver True/False
    def tiene_permiso(usuario, nombre_permiso):
        return True

    def get_by_email_and_pass(usuario, clave):
        return User.query.filter_by(usuario=usuario, clave=clave).first()

    
    def get_roles(id_usuario):
        return Usuario_tiene_rol.query.filter_by(usuario_id=id_usuario)
        #OK, ahora tengo una lista de 

    def agregar_rol(usuario, rol):
        rol.usuarios.append(usuario)
        db.session.commit()
        return True