from app.db import db
from datetime import datetime
from flask import session
from requests import get

tipos_de_centro = db.Table('centro_tiene_tipo',
                 db.Column('centro_id', db.Integer, db.ForeignKey(
                     'centro_de_ayuda.id'), primary_key=True),
                 db.Column('tipo_de_centro_id', db.Integer, db.ForeignKey(
                     'tipo_de_centro.id'), primary_key=True)
                 )


class Centro_de_ayuda(db.Model):
    __tablename__ = 'centro_de_ayuda'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    direccion = db.Column(db.String)
    telefono = db.Column(db.String)
    hora_de_apertura = db.Column(db.Time)
    hora_de_cierre = db.Column(db.Time)
    sitio_web = db.Column(db.String)
    email = db.Column(db.String)
    protocolo_de_vista = db.Column(db.String)
    coordenada_x = db.Column(db.Integer)
    coordenada_y = db.Column(db.Integer)
    historico = db.Column(db.Integer)
    tipos_de_centro = db.relationship('Tipo_de_centro', secondary=tipos_de_centro, backref=db.backref(
        'centros_de_ayuda_de_este_tipo', lazy=True), lazy='subquery')

    municipio_id = db.Column(db.Integer, db.ForeignKey('municipio.id'))
    municipio = db.relationship('Municipio', back_populates="centros_en_este_municipio")

    estado_id = db.Column(db.Integer, db.ForeignKey('estado_centro.id'))
    estado = db.relationship('Estado_centro', back_populates="centros_en_este_estado")

    def all():
        return Centro_de_ayuda.query.filter_by(historico=0).all()

    def borrar(id):
        centro = Centro_de_ayuda.query.filter_by(id=id).first()
        centro.historico = 1
        db.session.commit()
        return True

    def crear( nombre, direccion,telefono, hapertura, hcierre, email,sitio_web, corx, cory, lista_de_tipos, id_municipio, id_estado,protocolo='PDF', historico=0):
        tipos = []
        for tipo in lista_de_tipos:
            tipos.append(Tipo_de_centro.query.filter_by(id=tipo).first())
        print("Entre al crear del modelo")
        nuevo_centro = Centro_de_ayuda(nombre = nombre, direccion = direccion,telefono = telefono, hora_de_apertura = hapertura, hora_de_cierre=hcierre, email=email, sitio_web=sitio_web,tipos_de_centro=tipos, protocolo_de_vista=protocolo, coordenada_y=cory, coordenada_x=corx, historico = historico, municipio_id=id_municipio, estado_id=id_estado)#, ,o)
        print("Se creo en memoria el nuevo centro")
        db.session.add(nuevo_centro)
        db.session.commit()
        return True

    def existe_nombre(municipio_id,nombre):
        return Centro_de_ayuda.query.filter_by(municipio_id=municipio_id,nombre=nombre).first()
    
    def get_by_id(id):
        return Centro_de_ayuda.query.get(id)

    def hola_mundo():
        print("Hola mundo")
        return True

######################## MUNICIPIO ########################
class Municipio(db.Model):
    __tablename__ = 'municipio'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=True)
    centros_en_este_municipio = db.relationship("Centro_de_ayuda", back_populates="municipio")
    fase_id = db.Column(db.Integer)

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

######################## ESTADO ########################
class Estado_centro(db.Model):
    __tablename__ = 'estado_centro'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=True)
    centros_en_este_estado = db.relationship("Centro_de_ayuda", back_populates="estado")

    def all():
        return Estado_centro.query.all()
######################## ESTADO ########################