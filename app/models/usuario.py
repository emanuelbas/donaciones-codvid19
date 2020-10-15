from app.db import db
from sqlalchemy import update
from datetime import datetime


class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    clave = db.Column(db.String)

    def all():
        return User.query.all()

    #Completar
    def tiene_rol(id_usuario, nombre_rol):
    	return True

    #Completar
    def tiene_permiso(id_usuario, nombre_permiso):
    	return True
