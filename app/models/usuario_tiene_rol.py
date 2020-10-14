from app.db import db

class Usuario_tiene_rol(db.Model):
	__tablename__ = 'usuario_tiene_rol'
	id = db.Column(db.Integer(), primary_key=True)
	usuario_id = db.Column(bd.Integer(), db.ForeignKey('usuario.id', ondelete='CASCADE'))
	rol_id = db.Column(db.Integer(), db.ForeignKey('rol.id', ondelete='CASCADE'))