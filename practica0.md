# PRACTICA 0: GIT Y GITHUB

### Configuración del entorno.
Al no haber trabajado nunca con Git, el primer paso es el registro en GitHub desde su página web y cofiguración del perfil:
![Perfil Github](proyectoIV1617/imagenes/perfil Github.jpg)
Además, debemos generar una clave para que se identifique nuestro ordenador mediante el comando:
```
ssh-keygen -t rsa -C "correo@dominio.com"
```
Introducimos la clave generada (~/.ssh/id_rsa.pub) en el perfil de GitHub:
![Clave ssh en el perfil](proyectoIV1617/imagenes/clave ssh en perfil.jpg)
Continuamos con la instalación de Git en el PC desde el que se va a trabajar mediante los comandos (Ubuntu):
```
sudo apt-get install git
```
Una vez instalado, debemos configurarlo con nuestro nombre de usuario en GitHub y nuestra dirección de correo electrónico:
```
git config --global user.name "nombreUsuario"
git config --global user.email "email"
```

Una vez hecho todo esto tendremos todo listo para comenzar a trabajar.

### Creación del repositorio de la práctica.
Crearemos un repositorio con el nombre de la práctica, una breve descripción y elegiremos la licencia de nuestro proyecto:
![Creación del repositorio](proyectoIV1617/imagenes/creacion repositorio.jpg)
Creamos un "milestone" de la entrega de la práctica:
![Creación de milestone](proyectoIV1617/imagenes/creacion milestone.jpg)
Creamos las tareas para la entrega de la práctica:
![Creación de tareas](proyectoIV1617/imagenes/creacion de tareas.jpg)
Una vez creado, lo clonaremos a nuestro PC para trabajar con él:
![Clonación de repositorio](proyectoIV1617/imagenes/clonacion de repositorio.jpg)
Procedemos a cumplir con las tareas:

Ya tenemos lista la práctica.

### Creación de la documentación
Para almacenar los ficheros de la documentación emplearemos una rama llamada "hito0":
![Creación hito0](proyectoIV1617/imagenes/creacion hito0.jpg)
Podemos ver cómo se ha creado la nueva rama y nos encontramos en ella. 
Finalmente incluimos la carpeta de imágenes y el documento con el desarrollo de la práctica.
