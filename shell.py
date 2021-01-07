import os            #libreria de funciones del sistema operativo

#1. 	Copiar ( no puede ser una llamada a sistema a la función cp) - copiar
def copiar():

#2. 	Mover - mover
def mover():

#3. 	Renombrar - renombrar
def renombrar():

#4. 	Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
def listar():

#5. 	Crear un directorio - creardir
def creardir():

#6. 	Cambiar de directorio (no puede ser una llamada a sistema a la función cd) - ir
def ir():

#7. 	Cambiar los permisos sobre un archivo o un conjunto de archivos - permisos
def permisos():

#8. 	Cambiar los propietarios sobre un archivo o un conjunto de archivos. - propietario
def propietario():

#9. 	Cambiar la contraseña - contraseña
def contraseña():

#10.  Agregar usuario, y deben registrar los datos personales del mismo incluyendo su horario de trabajo y posibles lugares de conexión (ejemplo IPs o localhost). - usuario
def usuario():

#11.  El usuario debe poder levantar y apagar demonios dentro del sistema, utilizando una herramienta como service de CentOS. (no puede ser una llamada a sistema a la función service o systemctl)

#12.  Proveer la capacidad de poder ejecutar comandos del sistema, que no sean los comandos mencionados arriba.
def comandosys():

#13.  Registrar el inicio de sesión y la salida sesión del usuario. Se puede comparar con los registros de su horario cada vez que inicia/cierra la sesión y si esta fuera del rango escribir en el archivo de log (usuario_horarios_log) un mensaje que aclare que está fuera del rango y deben agregar el lugar desde donde realizó la conexión que también puede estar fuera de sus IPs habilitado.

#14.  Ejecutar una transferencia por ftp o scp, se debe registrar en el log Shell_transferencias del usuario. 

#el loop infinito utilizado para mantener el flujo del programa
def loop():
    while True:
        comando=input('$')

#se deben definir tambien el comando de ayuda y las funciones para escribir en el log
