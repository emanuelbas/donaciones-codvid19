from app.db import db
from sqlalchemy import update
from datetime import datetime
from flask import session


class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    clave = db.Column(db.String)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    email = db.Column(db.String)
    activo = db.Column(db.Integer)

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
    
    def new(us, cl, no, ap, em, ac):
        datos = User (usuario=us, clave=cl, nombre=no, apellido=ap, email=em, activo=ac)
        db.session.add (datos)
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
