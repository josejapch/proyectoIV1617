#!/bin/bash

#Variables de entorno para identificacion de Vagrant en Azure
export AZURE_TENANT_ID=
export AZURE_CLIENT_ID=
export AZURE_CLIENT_SECRET=
export AZURE_SUBSCRIPTION_ID=
export ANSIBLE_HOSTS=~/ansible_hosts

#Herramientas
apt-get update
apt-get vagrant
apt-get install nodejs-legacy
apt-get install npm
npm install -g azure-cli
vagrant plugin install vagrant-azure --plugin-version '2.0.0.pre1' --plugin-prerelease

#Creacion de maquina virtual en Azure
cd azure
cat ansible_hosts > ~/ansible_hosts
vagrant up --provider=azure
