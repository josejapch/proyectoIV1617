from django.shortcuts import render
from .models import Cola
from .forms import ConsultarColaForm
# Create your views here.

def home(request):
	return render(request, "home.html", {})

def consultar_cola(request):

	if request.method == "POST":
		form = ConsultarColaForm(request.POST)
		if form.is_valid():
			print request.POST["codigo_cola"]
			cola = Cola.objects.get(codigo_cola=request.POST["codigo_cola"])
			return render(request, "consultar_cola.html",{"cola":cola,"form":form})
	else:
		form = ConsultarColaForm()
	return render(request, "consultar_cola.html",{"form":form})
