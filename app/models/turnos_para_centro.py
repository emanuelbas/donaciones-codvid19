from app.db import db
from datetime import datetime, timedelta


class Turno(db.Model):
    __tablename__ = 'turnos_para_centro'
    id         = db.Column(db.Integer, primary_key=True)
    email      = db.Column(db.String)
    telefono   = db.Column(db.String)
    nombre     = db.Column(db.String)
    apellido   = db.Column(db.String)
    hora_ini   = db.Column(db.String)
    hora_fin   = db.Column(db.String)
    dia        = db.Column(db.String)
    borrado    = db.Column(db.Integer)
    centro_id  = db.Column(db.Integer)
    disponible = db.Column(db.Integer)

    def all():
        return Turno.query.all()

    def create(hi, hf, di, ce):
        em          = ""
        te          = ""
        act         = 1
        disponible  = 1
        nuevo_turno = Turno(email=em, telefono=te, hora_ini=hi, hora_fin=hf,
                            dia=di, borrado=act, centro_id=ce, disponible=disponible, nombre="sin nombre", apellido="sin apellido")
        db.session.add(nuevo_turno)
        db.session.commit()
        return True

    def create_reserva(i, em, te, ce):
        datos            = Turno.query.filter_by(centro_id=ce).first()
        datos.email      = em
        datos.telefono   = te
        datos.borrado    = 1
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

        datos            = Turno.query.filter_by(id=i).first()
        datos.email      = em
        datos.telefono   = te
        datos.borrado    = 1
        datos.disponible = disponible
        db.session.commit()
        return datos

    def delete(idx):
        turno            = Turno.query.filter_by(id=idx).first()
        turno.email      = ''
        turno.telefono   = ''
        turno.disponible = 1
        db.session.commit()
        return True

    def reservar_turno(centro_id,email_donante,nombre_donante,apellido_donante,telefono_donante,hora_inicio,hora_fin,fecha):
        turno = Turno.query.filter_by(centro_id=centro_id).filter_by(hora_ini=hora_inicio).filter_by(dia=fecha).first()
        if turno and turno.disponible:
            turno.email      = email_donante
            turno.telefono   = telefono_donante
            turno.nombre     = nombre_donante
            turno.apellido   = apellido_donante
            turno.disponible = 0
            db.session.commit()
            return True
        else:
            # Mod turnos - 07 February 2021 (Sunday)
            if turno:
                return False
            nuevo_turno = Turno(email=email_donante, telefono=telefono_donante, hora_ini=hora_inicio, hora_fin=hora_fin,
                dia=fecha, borrado=0, centro_id=centro_id, disponible=0, nombre=nombre_donante, apellido=apellido_donante)
            db.session.add(nuevo_turno)
            db.session.commit()
            # /Mod turnos
            return True

    def es_valido(centro_id, hora_inicio, fecha):
        turno = Turno.query.filter_by(centro_id=centro_id).filter_by(hora_ini=hora_inicio).filter_by(dia=fecha).filter_by(disponible=0).first()
        if turno:
            print("Se intento reservar un turno ocupado")
            return False
        else:
            return True

    def ultimos_turnos_para_centro(centro_id):
        turnos = Turno.query.filter_by(centro_id=centro_id).filter_by(dia>='1985-01-17').filter_by(disponible=0).all()
        return turnos

    def turnos_tomados_del_mes():
        # Tenemos que arreglar esta funcion en caso que se modifique el sistema de turnos
        # Ademas mejorarla para que devuelva solo los turnos del mes
        # fecha_hace_30_dias = datetime.now() - timedelta(days=30)
        # fecha_hace_30_dias = fecha_hace_30_dias.strftime("%m-%d-%Y")
        return Turno.query.filter_by(disponible=0).all()

    def turnos_tomados_para_centro(id_centro):
        return Turno.query.filter_by(centro_id=id_centro).filter_by(disponible=0).all()

    def get_proximos_turnos(centro_id):
        """ Devuelve un objeto paginable con los turnos de un centro para hoy y los proximos 2 dias """

        fecha_hoy = datetime.now().strftime("%Y-%m-%d")
        fecha_fin = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")
        return Turno.query.filter_by(centro_id=centro_id).filter(Turno.dia>=fecha_hoy).filter(Turno.dia<=fecha_fin).filter_by(disponible=0)

    def reservar(centro_id,email_donante,telefono_donante,hora_inicio,hora_fin,fecha):
        """ Se encarga de reservar el turno, en caso de no ser posible devuelve false """

        turno = Turno.query.filter_by(centro_id=centro_id).filter_by(hora_ini=hora_inicio).filter_by(dia=fecha).filter_by(disponible=0).first()
        if turno == None:
            return False

        nueva_reserva = Turno(
            email=email_donante,
            telefono=telefono_donante,
            hora_ini=hora_inicio,
            hora_fin=hora_fin,
            dia=fecha,
            borrado=0,
            centro_id=centro_id,
            disponible=0,
            nombre="sin nombre",
            apellido="sin apellido")
        db.session.add(nueva_reserva)
        db.session.commit()
        return True