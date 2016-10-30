from __future__ import unicode_literals

from django.db import models

class Cola(models.Model):
	""" Modelo de representacion de una cola.
	"""
	codigo_cola = models.CharField(default='',max_length=8, blank=False, null=False, unique=True, primary_key=True)
	propietario = models.CharField(default='',max_length=20, blank=False, null=False)
	nombre_cola = models.CharField(default='',max_length=20, blank=False, null=False)
	descripcion = models.CharField(max_length=140, blank=True, null=True)
	integrantes = models.IntegerField(default=0, editable = False, null=False)


	def __unicode__(self): #__str__ en python3
		return 'Codigo: %s Nombre: %s Propietario: %s Descripcion: %s'%(self.codigo_cola,self.nombre_cola,self.propietario,self.descripcion)


class Encolado(models.Model):
	""" Modelo de representacion de una persona que se ha unido a una cola.
	"""
	codigo_cola = models.ForeignKey('Cola')
	nick_encolado = models.CharField(max_length=20, blank=False, null=False)


	def __unicode__(self): #__str__ en python3
		return self.nick_encolado
