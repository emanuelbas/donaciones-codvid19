from app.db import db
from datetime import datetime


class Turno(db.Model):
    __tablename__ = 'turnos_para_centro'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    telefono = db.Column(db.String)
    hora_ini = db.Column(db.String)
    hora_fin = db.Column(db.String)
    dia = db.Column(db.String)
    borrado = db.Column(db.Integer)
    centro_id = db.Column(db.Integer)
    disponible = db.Column(db.Integer)

    def all():
        return Turno.query.all()

    def create(hi, hf, di, ce):
        em = ""
        te = ""
        act = 1
        disponible = 1
        nuevo_turno = Turno(email=em, telefono=te, hora_ini=hi, hora_fin=hf,
                            dia=di, borrado=act, centro_id=ce, disponible=disponible)
        db.session.add(nuevo_turno)
        db.session.commit()
        return True

    def create_reserva(i, em, te, ce):
        datos = Turno.query.filter_by(centro_id=ce).first()
        datos.email = em
        datos.telefono = te
        datos.borrado = 1
        datos.disponible = 0
        db.session.commit()
        return datos

    def get_by_id(id):
        return Turno.query.get(id)

    def select_turno(centro_id):
        return Turno.query.filter_by(centro_id=centro_id).all()

    def select_centro(ide):
        return Turno.query.filter_by(id=ide).all()

    def edit(i, em, te, disponible):

        datos = Turno.query.filter_by(id=i).first()
        datos.email = em
        datos.telefono = te
        datos.borrado = 1
        datos.disponible = disponible
        db.session.commit()
        return datos

    def delete(idx):
        turno = Turno.query.filter_by(id=idx).first()
        turno.email = ''
        turno.telefono = ''
        turno.disponible = 1
        db.session.commit()
        return True
