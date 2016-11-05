#!/bin/bash

heroku login;
status_login=$?

if [ "$status_login" -ne 0 ]; then
	echo 'Debe estar registrado en Heroku para hacer el despliegue.\n';
else
	heroku apps:create queueme --region eu;
	git add .;
	git commit -m "Despliegue en Heroku";
	git push heroku master;
	heroku config:set ON_HEROKU=1;
	heroku run python manage.py makemigrations;
	heroku run python manage.py migrate;
	heroku ps:scale web=1;
fi
