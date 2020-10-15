from flask import redirect, render_template, request, url_for, abort, session, flash, sessions
from flask.sessions import SecureCookieSessionInterface
from flaskps.db import get_db
from flaskps.models.user import User
from flaskps.models.conf import Conf
from flaskps.helpers.auth import authenticated


def usuarioTienePermisoDe(permisoParam):
    return (permisoParam in session.get('permisos'))

