from app.db import db
from datetime import datetime


class Configuracion(db.Model):
    __tablename__ = 'configuracion'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    descripcion = db.Column(db.String)
    mail = db.Column(db.String)
    activo = db.Column(db.Integer)
    cantPagina = db.Column(db.Integer)

    def all():
        return Configuracion.query.all()

    def edit(ti, de, ma, ac, cant):
        datos = Configuracion.query.filter_by(id=1).first()
        datos.titulo = ti
        datos.descripcion = de
        datos.mail = ma
        datos.activo = ac
        datos.cantPagina = cant

        db.session.commit()
        return datos

    def get_config():
        return Configuracion.query.filter_by(id=1).first()

    def habilitado():
        return Configuracion.query.filter_by(id=1).first().activo
