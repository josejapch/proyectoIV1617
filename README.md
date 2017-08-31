# QUEUEme. Proyecto IV 2016-2017

[![Build Status](https://travis-ci.org/josejapch/proyectoIV1617.svg?branch=master)](https://travis-ci.org/josejapch/proyectoIV1617)

[![Heroku](http://i66.tinypic.com/2d2ja74.jpg)](https://queueme.herokuapp.com/)

[![Docker](http://i63.tinypic.com/2dqt74p.jpg)](https://hub.docker.com/r/josejapch/proyectoiv1617/)

[Despliegue en Azure](http://winter-glitter-24.westeurope.cloudapp.azure.com/)

Repositorio de QUEUEme, práctica de la asignatura Infraestructura Virtual del Grado de Ingeniería Informática de la universidad de Granada.

**Nota Sobre la aplicación web: Por el momento no se va a continuar el desarrollo de la aplicación web en este repositorio. Este se mantendrá exclusivamente como entrega para la asignatura de Infraestructuras Virtuales.**

## **1. Introducción**

### 1.1. Descripción de la aplicación.
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

### 1.2. Infraestructura y herramientas.

La aplicación se desarrollará con el framework Django, lo que  implica el uso del lenguaje de programación Python. Además debemos automatizar tareas mediante scripts, realizar pruebas, realizar despliegue continuo... Las herramientas para realizar estas tareas se especificarán según vaya avanzando el proyecto.

Necesitaremos servidores para el frontend, despliegue de la aplicación, base de datos que gestionará las colas y registros de los usuarios, y gestión de correos.


## **2. Test e integración continua.**
#### 2.1. Test.
Se han realizado distintos test guiándonos con la [documentación de Django](https://docs.djangoproject.com/en/1.10/topics/testing/) (consultada en octubre de 2016). Utilizamos [unittest](https://docs.python.org/2/library/unittest.html), un módulo de Python para construir, ejecutar y automatizar test. Estos test actúan sobre models y views comprobando que se insertan elementos correctamente y se responde correctamente a las peticiones de las vistas. Podemos encontrarlos en [queue/tests.py](https://github.com/josejapch/proyectoIV1617/blob/master/queue/tests.py).

#### 2.2. Integración continua.
Para la intregación continua se ha empleado [Travis CI](https://travis-ci.org/). Para la configuración de Travis CI se ha creado el archivo [.travis.yml](https://github.com/josejapch/proyectoIV1617/blob/master/.travis.yml), el cual indica la versión de Python que utiliza la aplicación, el comando para la instalación de dependencias (a través del makefile de la aplicación web, que hace uso del archivo [requirements.txt](https://github.com/josejapch/proyectoIV1617/blob/master/requirements.txt)) y la ejecución de los test anteriormente comentados. Gracias al uso de Travis CI, cada vez que modifiquemos el repositorio (realicemos un push), se aplicarán los test de forma automática para comprobar que todo funciona correctamente. Al principio de este documento podemos ver la imagen de estado de la aplicación.

[Informacion extra: Configuración Travis CI](https://github.com/josejapch/documentacion-Proyecto-IV/blob/master/hito2.md)

#### 2.3. Makefile.
Se ha creado un [makefile](https://github.com/josejapch/proyectoIV1617/blob/master/Makefile) para automatizar instalación de herramientas y dependencias, y realización de test una vez clonado el proyecto:
- install: Instalar Python y pip.
- install-requirements: Instalar dependencias de la aplicación web (excepto Python).
- install-bd: Hacer migraciones de los modelos y crear la base de datos.
- test: Realizar los test de la aplicación.

## **3. Despliegue en un PaaS.**
Se ha realizado el despliegue de la aplicación en Heroku. Como base de datos se ha empleado la que la propia Heroku proporciona (PostgreSQL) y que está alojada en AmazonAWS. Además, se porporciona un [script](https://github.com/josejapch/proyectoIV1617/blob/master/deploy_heroku.sh) con el que automatizamos el despliegue (teniendo previamente una cuenta) en Heroku tras clonar el proyecto.

[Informacion extra: Despliegue y automatización en Heroku](https://github.com/josejapch/documentacion-Proyecto-IV/blob/master/hito3.md)

## **4. Entorno de pruebas.**
Para el entorno de pruebas se empleado Docker (gestor de contenedores). Se ha creado una imagen disponible en [dockerHub](https://hub.docker.com/r/josejapch/proyectoiv1617/), la cual contiene una versión ligera de la última versión disponible de Ubuntu, los requisitos de la aplicación y la aplicación web instalados.

Se puede obtener esta imagen usando (teniendo previamente Docker instalado) el comando: ```docker pull josejapch/proyectoiv1617```. La actualización de la imagen está sincronizada con GitHub, por lo que siempre contendrá la última versión de la aplicación web.

Además, se dispone del script [docker-up.sh](https://github.com/josejapch/proyectoIV1617/blob/master/docker-up.sh) para que, con un solo paso, se instale Docker (si no está instalado), se obtenga la imagen y se ejecute.

[Información extra: Creación de un entorno de pruebas para la aplicación usando contenedores](https://github.com/josejapch/documentacion-Proyecto-IV/blob/master/hito4.md)

## **5. Despliegue en un IaaS.**
Se ha realizado el despligue de la aplicación en Azure. Se ha empleado Vagrant como herramienta para crear la máquina virtual que contendrá la aplicación web, Ansible para su provisionamiento y Fabric para instalarla y ponerla en ejecución. El [Vagrantfile](https://github.com/josejapch/proyectoIV1617/blob/master/azure/Vagrantfile) para la creación de la máquina virtual, [playbook](https://github.com/josejapch/proyectoIV1617/blob/master/azure/queueplaybook.yml) de Ansible para el provisionamiento y [fabfile](https://github.com/josejapch/proyectoIV1617/blob/master/azure/fabfile.py) para el acceso remoto se encuentran en la carpeta [azure](https://github.com/josejapch/proyectoIV1617/tree/master/azure).

#### 5.1. Funciones fabfile.py
Las funciones de acceso remoto a través de Fabric disponibles son:
- install_app: Función para descargar e instalar la aplicación.
- app_up: Función para poner en marcha la aplicación.
- test_app: Función para ejecutar los test de la aplicación.
- app_down: Función para apagar la aplicación.
- delete_app: Función para eliminar la aplicación.

#### 5.2. Script
Además, se dispone del script [vm_azure.sh](https://github.com/josejapch/proyectoIV1617/blob/master/vm_azure.sh) para automatizar el proceso de creación de la máquina virtual en Azure. Este script deberá ser editado rellenando las variables de entorno con los datos de la cuenta de Azure propia del usuario.

También se proporciona el script [installandplay_azure.sh](https://github.com/josejapch/proyectoIV1617/blob/master/installandplay_azure.sh) para automatizar el proceso de descarga e instalación de la aplicación en la máquina virtual. El usuario deberá pasar como parámetro el nombre de DNS de la máquina virtual donde quiera instalarla.

[Información extra: Diseño del soporte virtual para el despliegue de una aplicación](https://github.com/josejapch/documentacion-Proyecto-IV/blob/master/hito5.md)

**Inscrito en el Certamen de Proyectos Libres de la UGR 2016-2017**