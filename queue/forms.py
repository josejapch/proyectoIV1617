from django import forms
from .models import Cola

class ConsultarColaForm(forms.ModelForm):
	""" Formulario para consultar la informacion de una cola aportando el codigo de la cola. 
	"""
	class Meta:
		model = Cola
		fields = ("codigo_cola",)

class RegistrarColaForm(forms.ModelForm):
	""" Formulario para consultar la informacion de una cola aportando el codigo de la cola. 
	"""
	class Meta:
		model = Cola
		fields = ("nombre_cola", "descripcion",)
