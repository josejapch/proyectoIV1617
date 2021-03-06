#Version de Ubuntu que queremos en la iamgen
FROM ubuntu:latest

#Encargado del mantenimiento
MAINTAINER Jose Javier Perez Checa <josepch@correo.ugr.es>

#Actualizamos repositorio
RUN apt-get update

#Instalamos git y descargamos el repositorio
RUN apt-get -y install git
RUN git clone https://github.com/josejapch/proyectoIV1617.git

#Instalamos python y pip por medio de nuestro Makefile
RUN apt-get install -y python-dev
RUN apt-get install -y libpq-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

#Instalamos los requisitos de nuestra aplicacion
RUN cd proyectoIV1617 && pip install -r requirements.txt

#Creamos la base de datos
RUN cd proyectoIV1617 && python manage.py makemigrations
RUN cd proyectoIV1617 && python manage.py migrate
