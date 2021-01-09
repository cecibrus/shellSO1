#!/usr/bin/env python3

import os            #libreria de funciones del sistema operativo --> https://docs.python.org/3/library/os.html
import sys
import cmd
import shutil
import subprocess
import getpass

#todos los comandos se deben poner en bloques de try except en caso de que salten errores,
#para que no muera todo el programa

class shellSO1(cmd.Cmd):
    intro=""" Bienvenidos a 
             _______  ______   _____     _______  ___   ___  _____  ___    ___
            |       ||      | /_    |   |       ||   | |   ||     ||   |  |   |
            |   ____||  __  |   |   |   |   ____||   |_|   || ____||   |  |   |
             \  \    | |  | |   |   |    \  \    |         || |___ |   |  |   |
              \  \   | |  | |   |   |     \  \   |    _    ||  ___||   |_ |   |_
             __\  \  | |__| |  _|   |_   __\  \  |   | |   || |___ |     ||     |
            |      | |      | |       | |      | |   | |   ||     ||     ||     |
            |______| |______| |_______| |______| |___| |___||_____||_____||_____|
            
        Trabajo de Sistemas Operativos 1. Cecilia Brusquetti y Gricelda Valdez
            """
    prompt='(SO1shell) $'
    file= None


    #lo que es path puede ser un string

    #1. 	Copiar ( no puede ser una llamada a sistema a la función cp) - copiar
    def do_copiar(self,arg):
        'Necesita dos argumentos, el archivo a copiar y el destino. Ejemplo: copiar <archivo> <path>'
        shutil.copy(*parse(arg))
        print('Con este comando se copia')
    #2. 	Mover - mover
    def do_mover(self,arg):
        #este si puede ser una llamada al sistema de la funcion mv 
        print('Con este comando se mueve')
    #3. 	Renombrar - renombrar
    def do_renombrar(self,arg):
        'Necesita dos argumentos, el nombre actual y el nombre nuevo. Ejemplo> renombrar <archivo> <nombrenuevo>'
        os.rename(*parse(arg))
        print('Con este comando se renombra')
    #4. 	Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
    def do_listar(self,arg):
        'No necesita argumentos, basta con introducir solo el comando'
        lista=os.listdir(path='.')
        print (lista)
        print('Con este comando se lista')
    #5. 	Crear un directorio - creardir
    def do_creardir(self,arg):
        'Se necesita el nombre del directorio a ser creado. Ejemplo: creardir <nombre>'
        path='./'+arg
        os.mkdir(path)
        print('Con este comando se crea un directorio')
    #6. 	Cambiar de directorio (no puede ser una llamada a sistema a la función cd) - ir
    def do_ir(self,arg):
        'Se necesita la direccion del directorio al que se quiere cambiar'
        #si el argumento esta vacio debe llevar a home
        os.chdir(arg)
        print('Con este comando se cambia de directorio')
    #7. 	Cambiar los permisos sobre un archivo o un conjunto de archivos - permisos
    def do_permisos(self,arg):
        'Se debe pasar el nombre del archivo y el modo. Ejemplo: permisos <archivo> <777>'
        os.chmod(*parse(arg))
        print('Con este comando se cambian permisos')
    #8. 	Cambiar los propietarios sobre un archivo o un conjunto de archivos. - propietario
    def do_propietario(self,arg):
        #os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)
        shutil.chown(*parse(arg)) #--> es de mas alto nivel que el de os
        print('Con este comando se cambian propietarios')
    #9. 	Cambiar la contraseña - contraseña
    def do_contrasenha(self,arg):
        'Cambia la contrasenha del usuario. Es necesario introducir solo el comando'
        os.system('passwd')
        print('Con este comando se cambia la contrasenha')
    #10.  Agregar usuario, y deben registrar los datos personales del mismo incluyendo su horario de trabajo y posibles lugares de conexión (ejemplo IPs o localhost). - usuario
    def do_usuario(self,arg):
        'Añade un nuevo usuario. Ejemplo: usuario <nuevoNombre>'
        comandon='useradd'+arg
        os.system(comandon)
        print('Con este comando se crea un usuario')
    #11.  El usuario debe poder levantar y apagar demonios dentro del sistema, utilizando una herramienta como service de CentOS. (no puede ser una llamada a sistema a la función service o systemctl)
    def do_demonio(self,arg):
        #se tienen que tener mas parametros como levantar y apagar
        #os.kill para apagar, se necesita el id de proceso
        #investigar como levantar
    #12.  Proveer la capacidad de poder ejecutar comandos del sistema, que no sean los comandos mencionados arriba.
    def do_shell(self, arg):
        'Ejecutar un comando ya existente de linux'
        print ("Ejecutando comando del shell:", arg)
        output = os.popen(arg).read()
        print (output)
    #13.  Registrar el inicio de sesión y la salida sesión del usuario. Se puede comparar con los registros de su horario cada vez que inicia/cierra la sesión y si esta fuera del rango escribir en el archivo de log (usuario_horarios_log) un mensaje que aclare que está fuera del rango y deben agregar el lugar desde donde realizó la conexión que también puede estar fuera de sus IPs habilitado.
    def registroUsuario():
        #se agrega la hora y la fecha
        #tambien se tienen que tener las IPs
    #14.  Ejecutar una transferencia por ftp o scp, se debe registrar en el log Shell_transferencias del usuario. 
    def do_transferencia(self,arg):
        #se debe revisar tambien si tiene otros parametros, como ftp o scp y de acuerdo a eso ver

def parse(arg):
    return tuple(arg.split())

if __name__=='__main__':
    shellSO1().cmdloop()
