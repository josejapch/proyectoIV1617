#!/bin/bash

ar=$#

if [ "$ar" -ne 1 ]; then
	echo "Ejecuta ./installandplay_azure.sh <nombre DNS de vm>"
else
	dns=$@
	cd azure
	fab -H vagrant@"$dns" install_app
	fab -H vagrant@"$dns" app_up
fi
