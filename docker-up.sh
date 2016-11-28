#!/bin/bash

wget -q0- https://get.docker.com/ | sh

service docker start

docker pull josejapch/proyectoiv1617

docker run -i -t mabarrbai/tuspachangas /bin/bash
