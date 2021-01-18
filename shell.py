#!/usr/bin/env python3

import os            #libreria de funciones del sistema operativo --> https://docs.python.org/3/library/os.html
import sys           #libreria del sistema
import cmd           #libreria para el formato de terminal
import shutil
import subprocess
import getpass
import signal
import socket
import datetime

#todos los comandos se deben poner en bloques de try except en caso de que salten errores,
#para que no muera todo el programa

class shellSO1(cmd.Cmd):
    intro=""" 
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
        comando=' copiar ' + arg
        try:
            shutil.copy(*parse(arg))
            registroLog(comando)
        except Exception as e:
            print(e)
            print("Ocurrio algun error o el comando no se esta utilizando correctamente. Vea la ayuda con help copiar")
            registroErrores(comando)
    #2. 	Mover - mover
    def do_mover(self,arg):
        #este si puede ser una llamada al sistema de la funcion mv 
        'Mueve un archivo de un directorio a otro. Ejemplo: mover <origen> <destino>'
        comando= ' mover ' + arg
        try:
            comandom='mv '+ arg
            os.system(comandom)
            registroLog(comando)
        except Exception as e:
            print(e)
            print("Ocurrio algun error o el comando no se esta utilizando correctamente. Vea la ayuda con help mover")
            registroErrores(comando)
    #3. 	Renombrar - renombrar
    def do_renombrar(self,arg):
        'Necesita dos argumentos, el nombre actual y el nombre nuevo. Ejemplo> renombrar <archivo> <nombrenuevo>'
        comando= ' renombrar ' + arg
        try:
            os.rename(*parse(arg))
            registroLog(comando)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help renombrar')
            registroErrores(comando)
    #4. 	Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
    def do_listar(self,arg):
        'No necesita argumentos, basta con introducir solo el comando'
        print(arg)
        comando=' listar ' + arg
        try:
            if(arg==''):
                lista=os.listdir(path='.')
            else:
                lista=os.listdir(path=arg)
            for x in lista:
                print(x)
            registroLog(comando)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help listar')
            registroErrores(comando)
    #5. 	Crear un directorio - creardir
    def do_creardir(self,arg):
        'Se necesita el nombre del directorio a ser creado, y es opcional una direccion. Ejemplo: creardir <nombre> </ejemplo/ejemplo2>'
        comando= ' creardir ' + arg
        try:
            args=parse(arg)
            if(len(args)==1): #significa que no especifico destino y se crea en el directorio actual
                path='./'+arg
            else:
                path=args[1]+args[0]
            os.mkdir(path)
            registroLog(comando)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help creardir')
            registroErrores(comando)
    #6. 	Cambiar de directorio (no puede ser una llamada a sistema a la función cd) - ir
    def do_ir(self,arg):
        'Se necesita la direccion del directorio al que se quiere cambiar'
        comando=' ir ' + arg
        #si el argumento esta vacio debe llevar a home
        try:
            if(arg==''):
                os.chdir('/home')
            else:
                os.chdir(arg)
            registroLog(comando)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help ir')
            registroErrores(comando)
    #7. 	Cambiar los permisos sobre un archivo o un conjunto de archivos - permisos
    def do_permisos(self,arg):
        'Cambia los permisos de un archivo. Se debe pasar el nombre del archivo y el modo. Ejemplo: permisos <archivo> <777>'
        comando= ' permisos ' + arg
        try: 
            os.chmod(*parse(arg))
            registroLog(comando)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help permisos')
            registroErrores(comando)
    #8. 	Cambiar los propietarios sobre un archivo o un conjunto de archivos. - propietario
    def do_propietario(self,arg):
        'Cambia el propietario de un archivo o un grupo de archivos. Ejemplo propietario <direccion> <nuevoPropietario>'
        #os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)
        comando= ' propietario ' + arg
        try:
            shutil.chown(*parse(arg)) #--> es de mas alto nivel que el de os
            registroLog(comando)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help propietario')
            registroErrores(comando)
    #9. 	Cambiar la contraseña - contraseña
    def do_contrasenha(self,arg):
        'Cambia la contrasenha del usuario. Es necesario introducir solo el comando'
        comando =' contrasenha ' + arg
        command = 'passwd ' + arg
        try:
            os.system(command)
            registroLog(comando)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help contrasenha')
            registroErrores(comando)
    #10.  Agregar usuario, y deben registrar los datos personales del mismo incluyendo su horario de trabajo y posibles lugares de conexión (ejemplo IPs o localhost). - usuario
    def do_usuario(self,arg):
        'Añade un nuevo usuario. Ejemplo: usuario <nuevoNombre>. Tambien se pueden agregar mas datos como horario de entrada y salida, y posibles direcciones de conexiones IP. Ejemplo: usuario <nombreUsuario> <horaEntrada> <horaSalida> <IP1> ... <IPn> en ese orden.'
        comando= ' usuario ' + arg
        try:
            args=parse(arg)
            if(len(args)>1):
                #si tiene mas de dos argumentos se registran los datos de entrada etc.
                registroUsuario(args)
            comandou='useradd -m ' + args[0] #se agrega el usuario con solo su direccion ip, los datos personales se registran en otro log
            os.system(comandou)
            registroLog(comando)
            print(comandou)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help usuario')
            registroErrores(comando)
    #11.  El usuario debe poder levantar y apagar demonios dentro del sistema, utilizando una herramienta como service de CentOS. (no puede ser una llamada a sistema a la función service o systemctl)
    def do_demonio(self,arg):
        'Levanta o apaga demonios. Necesita como parametro la accion y el ID de proceso en caso de apagar, y el archivo a ejecutar en caso de levantar. Ejemplo: demonio levantar/apagar <PID>'
        #se tienen que tener mas parametros como levantar y apagar
        comando= ' demonio ' + arg
        try:
            args=parse(arg)
            if(args[0]=='levantar'):
                try:
                    subprocess.Popen(args[1])
                    registroLog(comando)
                except Exception as e:
                    print(e)
                    print('Ocurrio un error o el parametro introducido es invalido. Vea la ayuda con help demonio')
                    registroErrores(comando)
            elif(args[0]=='apagar'):
                try:
                #SIGKILL no puede ser ignorado, SIGTERM si
                    pid=int(args[1])
                    os.kill(pid, signal.SIGTERM)
                    os.kill(pid, signal.SIGKILL)
                    registroLog(comando)
                except Exception as e:
                    print(e)
                    print('Ocurrio un error o el parametro introducido es invalido. Vea la ayuda con help demonio')
                    registroErrores(comando)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando se utilizo incorrectamente. Vea la ayuda con help demonio')
            registroErrores(comando)

        #os.kill para apagar, se necesita el id de proceso
        #investigar como levantar --> subprocess.Popen

    #12.  Proveer la capacidad de poder ejecutar comandos del sistema, que no sean los comandos mencionados arriba.
    def do_shell(self, arg):
        'Ejecutar un comando ya existente de linux'
        print ("Ejecutando comando del shell:", arg)
        output = os.popen(arg).read()
        print (output)
        comando= ' shell ' + arg
        #creo que no necesita manejo de errores ya que se hace solo

    #14.  Ejecutar una transferencia por ftp o scp, se debe registrar en el log Shell_transferencias del usuario. 
    def do_transferencia(self,arg):
        'Hace una transferencia ftp o scp. Por ejemplo  transferencia {ftp | scp}  <PARAMS>'
        #print("ftp o scp")
        comando = ' transferencia ' + arg
        try:
          os.system(arg)
          registroLog(comando)
          registroTransferencia(comando)
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help transferencia')
            registroErrores(comando)
    
    #15. Cerrar sesion y apagar la maquina       
    def do_apagar(self,arg):
        'Cierra sesion y apaga la maquina. Por ejemplo apagar <cant_minutos>'
        try:
            comando = ' apagar ' + arg
            llamada=['shutdown','-h']
            if(arg==''):
                llamada.append('now')
            else:
                llamada.append(arg)
            subprocess.call(llamada)
            registroLog(comando)
            registroLogout()
        except Exception as e:
            print(e)
            print('Ocurrio un error o el comando no se esta utilizando correctamente. Vea la ayuda con help apagar')
            registroErrores(comando)




#lee del log /var/log/usuario.log y retorna la linea que contiene al usuario del cual se pidio el horario e IPs

def read_personal(user):
    f = open('/var/log/usuario.log', 'r')
    while(True):
        linea = f.readline()
        lineas = parse(linea)
        if(len(lineas) >= 2):
            usr = lineas[1]
            if(usr == user ):
                f.close()
                return lineas
        if not linea:
            break
    f.close()
    return ""

 
#registro del login del usuario
def registroLogin():
    user = getpass.getuser()
    ipActual = str(socket.gethostbyname(socket.gethostname()))
    fecha = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    horaActual = str(datetime.datetime.now().strftime('%H:%M:%S'))
    info = read_personal(user)
    #Ejemplo:
    #info[0]= 'usuario: ' , info[1]= 'userlfs' , info[2]= 'horaEntrada: ' , info[3]= '10:30:00' , info[4]= 'horaSalida: ' ,
    # info[5]= '20:30:00' , info[6]= 'IP:' , info[7]= '192.168.43.170' .... info[n]= '192.168.43.50'
    #info = info.split()
    if(info == "" or info == '\n' or len(info) == 2):
        mensaje=' login ' + user + ' ' + fecha + '\n'
    else:
        horaEntrada = info[3]
        horaSalida = info[5]
        ip = False
        if not (horaEntrada <= horaActual <= horaSalida):
            men1 = ' (Login fuera de horario) '
        else: 
            men1 = ' (Login dentro de horario establecido) '
        for x in range(7, len(info)):
            if(ipActual == info[x]):
                ip = True
                break
        if not ip:
            men2 = ' (La Ip no coincide con su lista de IPs permitidas) '
        else:
           men2 = ' (La Ip coincide con su lista de IPs permitidas) ' 
        mensaje=' login ' + user + ' ' + fecha + ' -> ' + men1 + men2 + '\n'  
    f=open('/var/log/usuario_horarios_log', 'a')
    f.write(mensaje)
    f.close()


#registro del logout del usuario
def registroLogout():
    user = getpass.getuser()
    ipActual = str(socket.gethostbyname(socket.gethostname()))
    fecha = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    horaActual = str(datetime.datetime.now().strftime('%H:%M:%S'))
    info = read_personal(user)
    #Ejemplo:
    #info[0]= 'usuario: ' , info[1]= 'userlfs' , info[2]= 'horaEntrada: ' , info[3]= '10:30:00' , info[4]= 'horaSalida: ' ,
    # info[5]= '20:30:00' , info[6]= 'IP:' , info[7]= '192.168.43.170' .... info[n]= '192.168.43.50'
    #info = info.split()
    if(info == "" or info == '\n' or len(info) == 2):
        mensaje=' logout ' + user + ' ' + fecha + '\n'
    else:
        horaEntrada = info[3]
        horaSalida = info[5]
        ip = False
        if not (horaEntrada <= horaActual <= horaSalida):
            men1 = ' (Logout fuera de horario) '
        else: 
            men1 = ' (Logout dentro de horario establecido) '
        for x in range(7, len(info)):
            if(ipActual == info[x]):
                ip = True
                break
        if not ip:
            men2 = ' (La Ip no coincide con su lista de IPs permitidas) '
        else:
           men2 = ' (La Ip coincide con su lista de IPs permitidas) ' 
        mensaje=' logout ' + user + ' ' + fecha + ' -> ' + men1 + men2 + '\n'  
    f=open('/var/log/usuario_horarios_log', 'a')
    f.write(mensaje)
    f.close()

 #13.  Registrar el inicio de sesión y la salida sesión del usuario. Se puede comparar con los registros de su horario cada vez que inicia/cierra la sesión y si esta fuera del rango escribir en el archivo de log (usuario_horarios_log) un mensaje que aclare que está fuera del rango y deben agregar el lugar desde donde realizó la conexión que también puede estar fuera de sus IPs habilitado.
def registroUsuario(args):
    #args[1]-> hora de entrada
    #args[2]-> hora de salida
    #args[3]-> IP, hasta args[len(args)-1]
    print("aca se registran las actividades del usuario")
    #se agrega la hora de entrada/salida y las Ips permitidas
    mensaje = 'usuario: ' + args[0] + ' horaEntrada: ' + args[1] + ' horaSalida: ' + args[2] + ' IP: '
    for x in range(3, len(args)): #len(args)-1
        mensaje = mensaje + args[x] + ' '
    f=open('/var/log/usuario.log', 'a')
    f.write(mensaje)
    f.close()

#funcion para escribir en el log transferencias ftp/ scp realizadas
def registroTransferencia(command):
    fecha=datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    mensaje= fecha + command + '\n'
    f=open('/var/log/Shell_transferencias ', 'a')
    f.write(mensaje)
    f.close()

#funcion para escribir en el log los comandos
def registroLog(command):
    fecha=datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    mensaje= fecha + command + '\n'
    f=open('/var/log/registro.log', 'a')
    f.write(mensaje)
    f.close()

#funcion para registro del log de los errores
def registroErrores(command):
    fecha=datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
    mensaje= fecha + command + '\n'
    f=open('/var/log/shell/sistema_error.log', 'a')
    f.write(mensaje)
    f.close()

def parse(arg):
    return tuple(arg.split())

if __name__=='__main__':
    registroLogin()
    shellSO1().cmdloop()
