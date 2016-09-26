# PRACTICA 0: GIT Y GITHUB

## Configuración del entorno.
Al no haber trabajado nunca con Git, el primer paso es el registro en GitHub desde su página web y cofiguración del perfil:  
![img](https://github.com/josejapch/proyectoIV1617/blob/hito0/imagenes/perfil%20Github.jpg)  
Además, debemos generar una clave para que se identifique nuestro ordenador mediante el comando:  
```
ssh-keygen -t rsa -C "correo@dominio.com"
```
Introducimos la clave generada (~/.ssh/id_rsa.pub) en el perfil de GitHub:  
![img](https://github.com/josejapch/proyectoIV1617/blob/hito0/imagenes/clave%20ssh%20en%20perfil.jpg)  
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

## Creación del repositorio de la práctica.
Crearemos un repositorio con el nombre de la práctica, una breve descripción y elegiremos la licencia de nuestro proyecto:  
![img](https://github.com/josejapch/proyectoIV1617/blob/hito0/imagenes/creacion%20repositorio.jpg)  
Creamos un "milestone" de la entrega de la práctica:  
![img](https://github.com/josejapch/proyectoIV1617/blob/hito0/imagenes/creacion%20milestone.jpg)  
Creamos las tareas para la entrega de la práctica:  
![img](https://github.com/josejapch/proyectoIV1617/blob/hito0/imagenes/creacion%20de%20tareas.jpg)  
Una vez creado, lo clonaremos a nuestro PC para trabajar con él:  
![img](https://github.com/josejapch/proyectoIV1617/blob/hito0/imagenes/clonacion%20de%20repositorio.jpg)  
Procedemos a cumplir con las tareas:  
![img](https://github.com/josejapch/proyectoIV1617/blob/hito0/imagenes/realizacion%20de%20tareas.jpg)  

Ya tenemos lista la práctica.  

## Creación de la documentación.
Para almacenar los ficheros de la documentación emplearemos una rama llamada "hito0":  
![img](https://github.com/josejapch/proyectoIV1617/blob/hito0/imagenes/creacion%20hito0.jpg)  
Podemos ver cómo se ha creado la nueva rama y nos encontramos en ella.  
Finalmente incluimos la carpeta de imágenes y el documento con el desarrollo de la práctica.  
