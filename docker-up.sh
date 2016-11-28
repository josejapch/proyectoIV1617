#!/bin/bash

which docker

status_docker=$?

if ["$status_login" -ne 0]; then
	wget -qO- https://get.docker.com/ | sh;
fi

service docker start

docker pull josejapch/proyectoiv1617

docker run -i -t josejapch/proyectoiv1617 /bin/bash
