from app.db import db

class Permiso(db.Model):
    __tablename__= 'permiso'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)

    def get_by_name(nombre_permiso):
        return Permiso.query.filter_by(nombre=nombre_permiso).first()

    def all():
        return Permiso.query.all()