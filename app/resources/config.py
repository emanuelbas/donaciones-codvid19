from flask import render_template, abort, url_for, request, redirect, session, flash
from app.models.configuracion import Configuracion
from app.helpers import permisos
from datetime import date


def vista_configuracion():
    #permisos.validar_permisos('ver_configuracion_del_sitio');
    actual = Configuracion.all()
    if request.method == 'POST':
        datos = request.form
        #print(datos)  # se muestran todos los datos por termina
        Configuracion.edit(datos["titulo"], datos["descripcion"],
                    datos["mail"], datos["activo"], datos["cantPagina"])
        mensaje = "Se modifico la tabla configuracion correctamente"
        return render_template("configuracion/configuracion.html", actual=actual, mensaje=mensaje)
    elif request.method == 'GET':
        return render_template("configuracion/configuracion.html", actual=actual)
