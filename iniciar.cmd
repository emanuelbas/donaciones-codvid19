@ECHO OFF

COLOR CF
echo Bienvenido al sistema de gestion de comandos del Grupo 22
echo  
:rutina
SET /P OPT="Que desea hacer? ingrese b(Base de datos), f(Flask), v(Vue), s(Stop BD): "

GOTO CASE_%OPT%

ECHO Done.
EXIT /B


:CASE_b
  \xampp\mysql_start.bat
  GOTO END_CASE
:CASE_v
  cd web
  npm run serve
  GOTO END_CASE
:CASE_f
  flask run
  GOTO END_CASE
:CASE_s
  \xampp\mysql_stop.bat
  GOTO END_CASE
:DEFAULT_CASE
  ECHO Opcion desconocida "%OPT%"
  GOTO END_CASE
:END_CASE
  GOTO rutina