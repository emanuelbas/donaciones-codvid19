from app.db import db
from app.models.permiso import Permiso

permisos = db.Table('rol_tiene_permiso',
    db.Column('rol_id', db.Integer, db.ForeignKey('rol.id'), primary_key=True),
    db.Column('permiso_id', db.Integer, db.ForeignKey('permiso.id'), primary_key=True)
)

class Rol(db.Model):
	__tablename__= 'rol'
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String)
	permisos = db.relationship('Permiso', secondary=permisos, backref=db.backref('roles_con_el_permiso', lazy = True), lazy='subquery')

	def get_by_nombre(nombre_rol):
		return Rol.query.filter_by(nombre=nombre_rol).first()

	def all():
		return Rol.query.all()
