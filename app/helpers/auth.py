def authenticated(session):
    return session.get("user")
    
#agregado para el iniciar sesion
def cofigurated(session):
    return session.get('config')