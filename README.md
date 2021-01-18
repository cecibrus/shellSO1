# shellSO1 - Manual básico de uso.
Lo primero para empezar la instalación del shell es contar con el archivo shell.py en algun directorio. Es necesario descargarlo de https://github.com/cecibrus/shellSO1, colocarlo en un directorio y darle permisos de ejecución. Recomendamos descargarlo en el directorio /usr/local/bin, si se cuenta con la aplicación git, estos serían los pasos para instalar el shell:

cd /usr/local/bin/
git clone https://github.com/cecibrus/shellSO1.git   SO1Shell
cd SO1Shell/
mv shell.py /usr/local/bin/
cd ..
rm -Rf SO1Shell
sudo chmod 755 shell.py

El shell utiliza archivos de log para registrar los comandos, errores, login, etc. Estos se guardan en var/log. Estos archivos deben ser creados y darle permisos de escritura.
En registro.log está el historial de comandos exitosos.
En sistema_error.log está el historial de comandos que causaron errores.
En usuario_horarios_log se registran los inicios de sesión del usuario, indicando si entró fuera del horario de trabajo o desde una IP desconocida. 
En usuario.log están todos los datos del usuario, su horario de entrada y salida, etc.

Hay que tener permisos para poder escribir en /var/log, lo que se logra con los siguientes comandos:

sudo touch /var/log/filename.log 
sudo chmod 777 /var/log/filename.log

Eso anterior hay que hacer con cada uno de los archivos de log que se especificaron más arriba, reemplazando los nombres en filename.log que utilizará el shell para registrar los movimientos realizados.

Luego, es necesario hacer cambios en el archivo /etc/passwd para configurar el shell como predeterminado para un usuario en particular.
Abrir el archivo con vi o vim o algún otro editor de texto y en el usuario seleccionado, reemplazar /bin/bash por la dirección de shell.py. En nuestro caso /usr/local/bin/shell.py

Una vez que esto esté listo, es necesario reiniciar el sistema e ingresar con el usuario al que se le asignó el nuevo shell, y este debería cargarse automáticamente.

Se soportan los comandos “normales” del shell, como pwd,ls,mkdir,etc., como también los  nuevos comandos implementados.

Para saber cuales son estos comandos, puede utilizar el comando “help” o “?” por sí solo.

Para usar los comandos nuevos implementados, solo se escriben directamente. Para tener la ayuda de cada comando se escribe: help <comando>.

Con el comando ! se pueden ejecutar comandos del sistema. Utilizando ! <comando>.

