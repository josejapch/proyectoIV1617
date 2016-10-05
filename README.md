# QUEUEme. Proyecto IV 2016-2017

Repositorio de QUEUEme, práctica de la asignatura Infraestructura Virtual del Grado de Ingeniería Informática de la universidad de Granada.

##1. Introducción
###1.1. Descripción de la aplicación.
QUEUEme se trata de una aplicación web para la gestión de turnos. Su funcionamiento consiste en:


Un usuario se registra en la aplicación y puede crear una cola donde pueden unirse otros usuarios (no necesariamente registrados). Para esto, se le proporciona al usuario que ha creado la cola un código de identificación que tendrá que entregar a los usuarios que quieran unirse para identificarla en el sistema. Una vez llegue el momento de gestionar la cola, el usuario que la administre, podrá ver la información de los usuarios inscritos (solicitada en el momento de ingresar en la cola) e ir atendiéndolos. Una vez atendidos se eliminarán de la cola. Con la aplicación se podrá, por ejemplo: gestionar turnos de tutorías académicas, control de reservas de un producto en comercios, control de grupos que no necesariamente se necesite que estén en orden (pasar lista)...

Además de lo descrito anteriormente, el usuario registrado podrá:
- Consultar colas creadas.
- Eliminar colas creadas.
- Darse de baja.
- Modificar sus datos.

Un usuario no registrado podrá (además de unirse a una cola):
- Abandonar una cola.

*NOTA: Al estar aún en desarrollo puede que la funcionalidad de la aplicación se vea modificada añadiendole nuevas funciones.*

###1.2. Infraestructura y herramientas.

La aplicación se desarrollará con el framework Django, lo que  implica el uso del lenguaje de programación Python. Además debemos automatizar tareas mediante scripts, realizar pruebas, realizar despliegue continuo... Las herramientas para realizar estas tareas se especificarán según vaya avanzando el proyecto.

Necesitaremos servidores para el frontend, despliegue de la aplicación, base de datos que gestionará las colas y registros de los usuarios, y gestión de correos.



**Inscrito en el Certamen de Proyectos Libres de la UGR 2016-2017**
