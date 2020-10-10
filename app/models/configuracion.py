from app.db import db
from sqlalchemy import update
from datetime import datetime

# falta implementar consultas de bd para la funcionalidad


class Config(db.Model):
    __tablename__ = 'configuracion'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    descripcion = db.Column(db.String)
    mail = db.Column(db.String)
    activo = db.Column(db.Integer)
    cantPagina = db.Column(db.Integer)