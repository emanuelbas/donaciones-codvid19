from app.db import db
from sqlalchemy import update, ForeignKey, PrimaryKeyConstraint
from app.models.usuario import User
from app.models.rol import Rol

class Usuario_tiene_rol(db.Model):
    __tablename__ = 'usuario_tiene_rol'
    __table_args__ = (
        PrimaryKeyConstraint('usuario_id', 'rol_id'),
    )
    usuario_id = db.Column(db.Integer, ForeignKey(User.id))
    rol_id = db.Column(db.Integer, ForeignKey(Rol.id))

    def asignar_rol(idusuario, idrol):
        # agrega tupla a la tabla
        if not User_tiene_rol.query.filter_by(usuario_id=idusuario, rol_id=idrol).first():
            elemento = User_tiene_rol (usuario_id = idusuario, rol_id = idrol)
            db.session.add (elemento)
            db.session.commit() 
        return True


    def desasignar_rol(uid, rid):
        # borra tupla de la tabla
        if User_tiene_rol.query.filter_by(usuario_id=uid, rol_id=rid).first():
            User_tiene_rol.query.filter_by(usuario_id=uid, rol_id=rid).delete()
            db.session.commit()
        return True 

    def tiene_rol(uid, rid): 
    	# se fija si el usuario tiene el rol asociado y devuelve un bool
        return User_tiene_rol.query.filter_by(usuario_id=uid, rol_id=rid).first() != None