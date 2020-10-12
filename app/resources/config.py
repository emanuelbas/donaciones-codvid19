from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.configuracion import Config
from datetime import date


def vista_configuracion():
    actual = Config.all()
    if request.method == 'POST':
        datos = request.form
        print(datos)  # se muestran todos los datos por termina
        Config.edit(datos["titulo"], datos["descripcion"],
                    datos["mail"], datos["activo"], datos["cantPagina"])
        flash('Se actualizo la configuracion con exito')
    return render_template("configuracion/configuracion.html", actual=actual)
