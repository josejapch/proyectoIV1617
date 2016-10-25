""" Vistas de la aplicacion QUEUEme
"""

from django.shortcuts import render
from .models import Cola
from .forms import ConsultarColaForm

def home(request):

	""" Funcion para mostrar la pagina de inicio
	"""
	return render(request, "home.html", {})

def consultar_cola(request):
	""" Funcion para procesar el formulario para consultar informacion de una cola.
Si se encuentra la cola, se vuelve a la pagina del formulario con la informacion de la cola y se
muestra el formulario para una nueva consulta.
Si no se encuentra o aun no se ha realizado la consulta, se muestra el formulario de la consulta.
	"""
	if request.method == "POST":
		form = ConsultarColaForm(request.POST)
		if form.is_valid():
			try:
				cola = Cola.objects.get(codigo_cola=request.POST["codigo_cola"])
				return render(request, "consultar_cola.html",{"cola":cola,"form":form})
			except Cola.DoesNotExist:
				return render(request, "consultar_cola.html",{"form":form})
				
	else:
		form = ConsultarColaForm()
	return render(request, "consultar_cola.html",{"form":form})
