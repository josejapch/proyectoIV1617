from django import forms
from .models import Cola

class ConsultarColaForm(forms.ModelForm):

	class Meta:
		model = Cola
		fields = ("codigo_cola",)
