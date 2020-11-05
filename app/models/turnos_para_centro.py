from app.db import db
from datetime import datetime


class Turno(db.Model):
    __tablename__ = 'turnos_para_centro'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    bloque_turno = db.Column(db.String)
    dia = db.Column(db.String)
    borrado = db.Column(db.Integer)
    centro_id = db.Column(db.Integer)

    def all():
        return Turno.query.all()

    def create(em, bl, di, ce):
        act = 1
        nuevo_turno = Turno(email=em, bloque_turno=bl,
                            dia=di, borrado=act, centro_id=ce)
        db.session.add(nuevo_turno)
        db.session.commit()
        return True

    def get_by_id(id):
        return Turno.query.get(id)
    
    def select_turno(centro_id):
         return Turno.query.filter_by(centro_id = centro_id).all()

    def select_centro(ide):
        return Turno.query.filter_by(id = ide).all()
    
    def edit(i, em, bl, di):

        datos = Turno.query.filter_by(id=i).first()
        datos.email = em
        datos.bloque_turno = bl
        datos.dia = di
        datos.borrado = 1
        db.session.commit()
        return datos
    
    def delete(idx):
        turno = Turno.query.filter_by(id=idx).first()
        turno.borrado = 0
        db.session.commit()
        return True
