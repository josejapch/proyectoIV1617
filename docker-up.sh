#!/bin/bash

wget -qO- https://get.docker.com/ | sh

service docker start

docker pull josejapch/proyectoiv1617

docker run -i -t josejapch/proyectoiv1617 /bin/bash
