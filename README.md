# QUEUEme. Proyecto IV 2016-2017

[![Build Status](https://travis-ci.org/josejapch/proyectoIV1617.svg?branch=master)](https://travis-ci.org/josejapch/proyectoIV1617)

Repositorio de QUEUEme, práctica de la asignatura Infraestructura Virtual del Grado de Ingeniería Informática de la universidad de Granada.

## **1. Introducción**
####1.1. Descripción de la aplicación.
QUEUEme se trata de una aplicación web para la gestión de turnos. Su funcionamiento consiste en:


Un usuario se registra en la aplicación y puede crear una cola donde pueden unirse otros usuarios (no necesariamente registrados). Para esto, se le proporciona al usuario que ha creado la cola un código de identificación que tendrá que entregar a los usuarios que quieran unirse para identificarla en el sistema. Una vez llegue el momento de gestionar la cola, el usuario que la administre, podrá ver la información de los usuarios inscritos (solicitada en el momento de ingresar en la cola) e ir atendiéndolos. Una vez atendidos se eliminarán de la cola. Con la aplicación se podrá, por ejemplo: gestionar turnos de tutorías académicas, control de reservas de un producto en comercios, control de grupos que no necesariamente se necesite que estén en orden (pasar lista)...

Además de lo descrito anteriormente, el usuario registrado podrá:
- Consultar colas creadas.
- Eliminar colas creadas.
- Darse de baja.
- Modificar sus datos.

Un usuario no registrado podrá (además de unirse a una cola):
- Abandonar una cola.
- Consultar información de una cola a través de su código de cola.

*NOTA: Al estar aún en desarrollo puede que la funcionalidad de la aplicación se vea modificada añadiendole nuevas funciones.*

####1.2. Infraestructura y herramientas.

La aplicación se desarrollará con el framework Django, lo que  implica el uso del lenguaje de programación Python. Además debemos automatizar tareas mediante scripts, realizar pruebas, realizar despliegue continuo... Las herramientas para realizar estas tareas se especificarán según vaya avanzando el proyecto.

Necesitaremos servidores para el frontend, despliegue de la aplicación, base de datos que gestionará las colas y registros de los usuarios, y gestión de correos.

## **2. Test e integración continua.**
####2.1. Test.
Se han realizado distintos test guiándonos con la [documentación de Django](https://docs.djangoproject.com/en/1.10/topics/testing/) (consultada en octubre de 2016). Estos test actúan sobre models y views comprobando que se insertan elementos correctamente y se responde correctamente a las peticiones de las vistas. Podemos encontrarlos en [queue/tests.py](https://github.com/josejapch/proyectoIV1617/blob/master/queue/tests.py).

####2.2. Integración continua.
Para la intregación continua se ha empleado [Travis CI](https://travis-ci.org/). Para la integración en Travis CI se ha creado el archivo [.travis.yml](https://github.com/josejapch/proyectoIV1617/blob/master/.travis.yml), el cual indica la versión de Python que se ha empleado, el comando para la instalación de dependencias (a través del archivo [requirements.txt](https://github.com/josejapch/proyectoIV1617/blob/master/requirements.txt)) y la ejecución de los test anteriormente comentados. Gracias al uso de Travis CI, cada vez que modifiquemos el repositorio (realicemos un push), se aplicarán los test de forma autmática para comprobar que todo funciona correctamente. Al principio de este documento podemos ver la imagen de estado de la aplicación.

[Informacion extra: Configuración Travis CI](https://github.com/josejapch/documentacion-Proyecto-IV/blob/master/hito2.md)

####2.3. Makefile.
Se ha creado un [makefile](https://github.com/josejapch/proyectoIV1617/blob/master/Makefile) para automatizar instalación de herramientas y dependencias, y realización de test una vez clonado el proyecto.

**Inscrito en el Certamen de Proyectos Libres de la UGR 2016-2017**
