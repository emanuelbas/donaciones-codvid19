from app.db import db
from datetime import datetime


class Turnos_para_cada_centro(db.Model):
    __tablename__ = 'turnos_para_cada_centro'
    id = db.Column(db.Integer, primary_key=True)
    turno_id = db.Column(db.Integer)
    centro_id = db.Column(db.Integer)

    def create(c_id, t_id):
        dato = Turnos_para_cada_centro(turno_id=t_id, centro_id=c_id)
        db.session.add(dato)
        db.session.commit()
        return True
    
    def get_centro_id(centro_id):
        return Turnos_para_cada_centro.query.filter_by(centro_id=centro_id)
    
    def get_turno_id(turno_id):
        return Turnos_para_cada_centro.query.filter_by(turno_id=turno_id)
    
    def edit(i, c_id, t_id):

        datos = Turnos_para_cada_centro.query.filter_by(id=i).first()
        datos.turno_id = t_id
        datos.cetro_id = c_id
        db.session.commit()
        return datos