from app.db import db
from datetime import datetime


class Turno(db.Model):
    __tablename__ = 'turnos_para_centro'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    bloque_turno = db.Column(db.String)
    dia = db.Column(db.String)
    activo = db.Column(db.Integer)

    def all():
        return Turno.query.all()

    def create(em, bl, di):
        act = 1
        nuevo_turno = Turno(email=em, bloque_turno=bl, dia=di, activo=act)
        db.session.add(nuevo_turno)
        db.session.commit()
        return True

    def get_by_id(id):
        return Turno.query.get(id)
    
    def edit(i, em, bl, di):

        datos = Turno.query.filter_by(id=i).first()
        datos.email = em
        datos.bloque_turno = bl
        datos.dia = di
        datos.activo = 1
        db.session.commit()
        return datos
    
    def delete(idx):
        turno = Turno.query.filter_by(id=idx).first()
        turno.activo = 0
        db.session.commit()
        return True
