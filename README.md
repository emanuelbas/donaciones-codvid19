# Donaciones CODVID-19

Este proyecto presenta un prototipo de aplicación web que busca dar solución al sistema de gestión de Centros de Ayuda de la Provincia de Buenos Aires, permitiendo ser utilizado por Operadores y Administradores así como también su versión pública por usuarios no registrados para solicitar turnos.
El proyecto está desarrollado con Flask para la parte privada y Vue.js para la parte pública, se desarrolla una API y se utiliza una Base de Datos MySQL.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._


### Pre-requisitos 📋

_Para instalar el software es necesario contar con los siguientes requisitos_

* XAMP
* Python3
* Node.js

### Instalación 🔧

Clonar el proyecto 

```
git clone https://github.com/emanuelbas/donaciones-codvid19.git
```

Importar la base de datos desde el archivo /db/grupo22.sql
Ajustar las credenciales en el archivo /config.py

Instalar las dependencias de la parte privada

```
cd donaciones-codvid19
pip3 install -r requirements.txt
```
Instalar las dependencias de la parte pública

```
cd web
npm install
```

## Construido con 🛠️

* [Vue.js](https://vuejs.org/) - The Progressive JavaScript Framework
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Web development, one drop at a time
* [XAMP](https://www.apachefriends.org/es/index.html) - Apache + MariaDB + PHP + Perl
* [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL Toolkit and Object Relational Mapper
* [Leaflet](https://leafletjs.com/) - An open-source JavaScript library for mobile-friendly interactive maps
* [Axios](https://www.npmjs.com/package/axios) - Promise based HTTP client for the browser and node.js
* [Bootstrap](https://getbootstrap.com/) - Build fast, responsive sites with Bootstrap

## Autores ✒️

* **Mayra Anabela Luengo Orellano**
* **Emanuel Bastons**
* **Maximiliano Francesconi**
* **Hugo Dario Contrerai**