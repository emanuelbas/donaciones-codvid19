from app.db import db

class Rol(db.Model):
	__tablename__= 'rol'
	id = db.column(db.Integer, primary_key = True)
	nombre = db.column(db.String)

    def get_by_nombre(nombre_rol):
        return Rol.query.filter_by(nombre=nombre_rol).first()

    def all():
		return Rol.query.all()
