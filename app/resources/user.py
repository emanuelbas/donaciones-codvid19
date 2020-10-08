from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.usuario import User
from datetime import date


def quienesomos():
    usuario = User.all()
    print(usuario)
    return render_template('quienesomos.html', usuario=usuario)

def centros():
    return render_template('centros.html', methods=["POST", "GET"])

def login():
    return render_template('/auth/login.html')