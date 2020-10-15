def authenticated(session):
    return session.get("usuario")
    
#agregado para el iniciar sesion
def cofigurated(session):
    return session.get('config')