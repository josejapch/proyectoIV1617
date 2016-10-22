from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from queue.models import Cola, Encolado
from queue.views import home, consultar_cola

# Create your tests here.

class TestModelos(TestCase):
		
	def test_insertar_modelo_cola(self):
		""" Comprobar las inserciones de colas """

		cola = Cola(codigo_cola="codTest", propietario="propTest",nombre_cola="nomTest",descripcion="Esto es un test")
		cola.save()

		cComp = Cola.objects.get(codigo_cola="codTest")

		self.assertEqual(cola.codigo_cola,cComp.codigo_cola)
		self.assertEqual(cola.propietario,cComp.propietario)
		self.assertEqual(cola.nombre_cola,cComp.nombre_cola)
		self.assertEqual(cola.descripcion,cComp.descripcion)

		print "OK. Se ha insertado la cola correctamente."


	def test_insertar_modelo_encolado(self):
		""" Comprobar las inserciones de encolados """

		encolado = Encolado(codigo_cola="codTest",nick_encolado="nickTest")
		encolado.save()

		enComp = Encolado.objects.get(codigo_cola="codTest")

		self.assertEqual(encolado.codigo_cola,enComp.codigo_cola)
		self.assertEqual(encolado.nick_encolado,enComp.nick_encolado)

		print "OK. Se ha insertado el encolado correctamente."



class TestViews(TestCase):

	def test_home(self):
		""" Comprobar que una peticion get de home obtiene el codigo de respuesta 200 (exito)"""

		cliente = Client()
		respuesta = cliente.get(reverse("home"))

		self.assertEqual(respuesta.status_code,200)

		print "OK. Se ha respondido con exito a la peticion get de home."


	def test_consultar_cola(self):
		""" Comprobar que una peticion get de consultar_cola obtiene el codigo de respuesta 200 (exito)"""

		cliente = Client()
		respuesta = cliente.get(reverse("consultar_cola"))

		self.assertEqual(respuesta.status_code,200)

		print "OK. Se ha respondido con exito a la peticion get de consultar_cola."


	def test_formulario_consultar_cola(self):
		""" Comprobar que el formulario de consultar_cola obtiene una respuesta correcta al introducir un elemento que no existe."""

		cliente = Client()
		respuesta = cliente.post("/consultar_cola/",{"codigo_cola":"codTest4"})

		self.assertEqual(respuesta.status_code,200)

		print "OK. Se ha respondido con exito a la peticion post de consultar_cola."


if __name__ == '__main__':
	unittest.main()
