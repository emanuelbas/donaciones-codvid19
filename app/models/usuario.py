from app.db import db
from sqlalchemy import update
from datetime import datetime
from flask import session

class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    clave = db.Column(db.String)
    def all():
        return User.query.all()


    #COMPLETAR: Debe devolver True/False
    def tiene_rol(usuario, nombre_rol):
    	return True

    #COMPLETAR: Debe devolver True/False
    def tiene_permiso(usuario, nombre_permiso):
    	return True

    def get_by_email_and_pass(usuario, clave):
                return User.query.filter_by(usuario=usuario, clave=clave).first()

