import os            #libreria de funciones del sistema operativo
import sys
import cmd

class shellSO1(cmd.Cmd):
    intro='Este es el shell de SO1'
    prompt='(SO1shell) $'
    file= None

    #1. 	Copiar ( no puede ser una llamada a sistema a la función cp) - copiar
    def do_copiar(self,arg):
        'Copia de un lugar a otro'
        print('Con este comando se copia')
    #2. 	Mover - mover
    def do_mover(self,arg):
        print('Con este comando se mueve')
    #3. 	Renombrar - renombrar
    def do_renombrar(self,arg):
        print('Con este comando se renombra')
    #4. 	Listar un directorio (no puede ser una llamada a sistema a la función ls) - listar
    def do_listar(self,arg):
        print('Con este comando se lista')
    #5. 	Crear un directorio - creardir
    def do_creardir(self,arg):
        print('Con este comando se crea un directorio')
    #6. 	Cambiar de directorio (no puede ser una llamada a sistema a la función cd) - ir
    def do_ir(self,arg):
        print('Con este comando se cambia de directorio')
    #7. 	Cambiar los permisos sobre un archivo o un conjunto de archivos - permisos
    def do_permisos(self,arg):
        print('Con este comando se cambian permisos')
    #8. 	Cambiar los propietarios sobre un archivo o un conjunto de archivos. - propietario
    def do_propietario(self,arg):
        print('Con este comando se cambian propietarios')
    #9. 	Cambiar la contraseña - contraseña
    def do_contraseña(self,arg):
        print('Con este comando se cambia la contrasenha')
    #10.  Agregar usuario, y deben registrar los datos personales del mismo incluyendo su horario de trabajo y posibles lugares de conexión (ejemplo IPs o localhost). - usuario
    def do_usuario(self,arg):
        print('Con este comando se crea un usuario')
    #11.  El usuario debe poder levantar y apagar demonios dentro del sistema, utilizando una herramienta como service de CentOS. (no puede ser una llamada a sistema a la función service o systemctl)

    #12.  Proveer la capacidad de poder ejecutar comandos del sistema, que no sean los comandos mencionados arriba.

    #13.  Registrar el inicio de sesión y la salida sesión del usuario. Se puede comparar con los registros de su horario cada vez que inicia/cierra la sesión y si esta fuera del rango escribir en el archivo de log (usuario_horarios_log) un mensaje que aclare que está fuera del rango y deben agregar el lugar desde donde realizó la conexión que también puede estar fuera de sus IPs habilitado.

    #14.  Ejecutar una transferencia por ftp o scp, se debe registrar en el log Shell_transferencias del usuario. 

def parse(arg):
    return tuple(map(int,arg.split()))

if __name__=='__main__':
    shellSO1().cmdloop()