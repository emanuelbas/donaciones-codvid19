from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.configuracion import Config
from datetime import date

def vista_configuracion():
    return render_template('/configuracion/configuracion.html')