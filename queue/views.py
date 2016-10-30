""" Vistas de la aplicacion QUEUEme
"""

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Cola
from .forms import ConsultarColaForm, RegistrarColaForm
import string
import random

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
		#if form.is_valid():
		try:
			cola = Cola.objects.get(pk=request.POST["codigo_cola"])
			return render(request, "consultar_cola.html",{"cola":cola,"form":form})
		except Cola.DoesNotExist:
			error = "La cola que ha introducido no existe."
			return render(request, "consultar_cola.html",{"error":error,"form":form})
				
	else:
		form = ConsultarColaForm()
	return render(request, "consultar_cola.html",{"form":form})


def generar_codigo():
	""" Funcion para crear codigo aleatorio de una cola
	"""
	codigo = ""
	for i in range(8):
		codigo = codigo + (random.choice(string.ascii_uppercase + string.digits))

	return codigo

def registrar_cola(request):
	""" Funcion para procesar el formulario para registrar una cola.
	"""
	if request.method == "POST":
		form = RegistrarColaForm(request.POST)
		if form.is_valid():
			#try:
				post = form.save(commit=False)
				post.propietario = (request.user).get_username()
				codigo = generar_codigo()
		
				existe = True

				while (existe):
					try:
						cola = Cola.objects.get(codigo_cola=codigo)
					except Cola.DoesNotExist:
						existe = False

					if existe:
						codigo = generar_codigo(post.propietario, post.nombre_cola)
	
				post.codigo_cola = codigo

				post.save()
				result = "Se ha creado la cola correctamente con el codigo " + codigo
				return render(request, "registrar_cola.html",{"resultado":result,"form":form})
			#except:
				result = "No se ha podido crear la cola."
				return render(request, "registrar_cola.html",{"resultado":result,"form":form})
				
	else:
		form = RegistrarColaForm()
	return render(request, "registrar_cola.html",{"form":form})
