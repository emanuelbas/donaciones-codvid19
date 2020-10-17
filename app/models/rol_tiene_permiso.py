from app.db import db
from app.models.rol import Rol
from app.models.permiso import Permiso
from sqlalchemy import ForeignKey, PrimaryKeyConstraint

class Rol_tiene_permiso(db.Model):
    __tablename__= 'rol_tiene_permiso'
    __table_args__ = (
        PrimaryKeyConstraint('id_rol', 'id_permiso'),
    )
    id_rol = db.Column(db.Integer,ForeignKey(Rol.id))
    id_permiso = db.Column(db.Integer,ForeignKey(Permiso.id))
    
    def tiene_permiso(idrol,idpermiso):
        return Permiso.query.filter_by(id_rol=idrol, id_permiso=idpermiso).first() != None

    def all():
        return rol_tiene_permiso.query.all()