from app.db import db
from sqlalchemy import update
from datetime import datetime


class User(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String)
    clave = db.Column(db.String)

    def all():
        return User.query.all()

    #Relaciones
    roles = db.relationship('Role', secondary='user_roles')

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)

class UserRoles(db.Model):
	__tablename__ = 'user_roles'
	id = db.Column(db.Integer(), primary_key=True)
	user_id = db.Column(bd.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
	role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))