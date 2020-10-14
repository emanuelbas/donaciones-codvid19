from app.db import db
from sqlalchemy import update
from datetime import datetime

class Rol(db.Model):
	__tablename__ = 'rol'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), unique=True)