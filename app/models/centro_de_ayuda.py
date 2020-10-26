from app.db import db
from datetime import datetime
from flask import session

tipos_de_centro = db.Table('centro_tiene_tipo',
                 db.Column('centro_id', db.Integer, db.ForeignKey(
                     'centro_de_ayuda.id'), primary_key=True),
                 db.Column('tipo_de_centro_id', db.Integer, db.ForeignKey(
                     'tipo_de_centro.id'), primary_key=True)
                 )


class Centro_de_ayuda(db.Model):
    __tablename__ = 'centro_de_ayuda'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=True)
    direccion = db.Column(db.String)
    telefono = db.Column(db.String)
    hora_de_apertura = db.Column(db.String)
    hora_de_cierre = db.Column(db.String)
    sitio_web = db.Column(db.String)
    email = db.Column(db.String)
    estado = db.Column(db.String)
    protocolo_de_vista = db.Column(db.String)
    coordenada_x = db.Column(db.Integer)
    coordenada_y = db.Column(db.Integer)
    historico = db.Column(db.Integer)
    tipos_de_centro = db.relationship('Tipo_de_centro', secondary=tipos_de_centro, backref=db.backref(
        'centros_de_ayuda_de_este_tipo', lazy=True), lazy='subquery')

    municipio_id = db.Column(db.Integer, db.ForeignKey('municipio.id'))
    municipio = db.relationship('Municipio', back_populates="centros_en_este_municipio", lazy='subquery')

    def all():
        return Centro_de_ayuda.query.filter_by(historico=0).all()

######################## MUNICIPIO ########################
class Municipio(db.Model):
    __tablename__ = 'municipio'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=True)
    centros_en_este_municipio = db.relationship("Centro_de_ayuda", back_populates="municipio")

    def all():
        return Municipio.query.all()
######################## MUNICIPIO ########################


######################## TIPO DE CENTRO ########################
class Tipo_de_centro(db.Model):
    __tablename__ = 'tipo_de_centro'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=True)

    def all():
        return Tipo_de_centro.query.all()
######################## TIPO DE CENTRO ########################