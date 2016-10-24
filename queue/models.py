from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cola(models.Model):
	""" Modelo de representacion de una cola.
	"""
	codigo_cola = models.CharField(max_length=20, blank=False, null=False)
	propietario = models.CharField(max_length=20, blank=False, null=False)
	nombre_cola = models.CharField(default='',max_length=20, blank=False, null=False)
	descripcion = models.CharField(max_length=140, blank=True, null=True)

	def __unicode__(self): #__str__ en python3
		return 'Codigo: %s Nombre: %s Propietario: %s Descripcion: %s'%(self.codigo_cola,self.nombre_cola,self.propietario,self.descripcion)

class Encolado(models.Model):
	""" Modelo de representacion de una persona que se ha unido a una cola.
	"""
	codigo_cola = models.CharField(max_length=20, blank=False, null=False)
	nick_encolado = models.CharField(max_length=20, blank=False, null=False)

	def __unicode__(self): #__str__ en python3
		return self.nick
