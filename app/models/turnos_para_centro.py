from app.db import db
from datetime import datetime, timedelta


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

    def reservar_turno(centro_id,email_donante,telefono_donante,hora_inicio,hora_fin,fecha):
        turno = Turno.query.filter_by(centro_id=centro_id).filter_by(hora_ini=hora_inicio).filter_by(dia=fecha).first()
        if turno and turno.disponible:
            turno.email = email_donante
            turno.telefono = telefono_donante
            turno.disponible = 0
            db.session.commit()
            return True
        else:
            return False

    def es_valido(centro_id, hora_inicio, fecha):
        turno = Turno.query.filter_by(centro_id=centro_id).filter_by(hora_ini=hora_inicio).filter_by(dia=fecha).first()
        if turno:
            return True
        else:
            return False

    def ultimos_turnos_para_centro(centro_id):
        turnos = Turno.query.filter_by(centro_id=centro_id).filter_by(dia>='1985-01-17').filter_by(disponible=0).all()
        return turnos

    def turnos_tomados_del_mes():
        # Tenemos que arreglar esta funcion en caso que se modifique el sistema de turnos
        # Ademas mejorarla para que devuelva solo los turnos del mes
        # fecha_hace_30_dias = datetime.now() - timedelta(days=30)
        # fecha_hace_30_dias = fecha_hace_30_dias.strftime("%m-%d-%Y")
        return Turno.query.filter_by(disponible=0).all()

    def turnos_para_centro(id_centro):
        return Turno.query.filter_by(centro_id=id_centro).all()