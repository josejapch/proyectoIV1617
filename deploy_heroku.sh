#!/bin/bash

heroku login;
heroku apps:create queueme --region eu;
git add .;
git commit -m "Despliegue en Heroku";
git push heroku master;
heroku config:set ON_HEROKU=1;
heroku python manage.py makemigrations;
heroku python manage.py migrate;
heroku ps:scale web=1;

