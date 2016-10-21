from django.contrib import admin
from .models import Cola, Encolado
# Register your models here.

class AdminCola(admin.ModelAdmin):
	list_display = ["codigo_cola","propietario","nombre_cola","descripcion"]
	class Meta:
		model = Cola

class AdminEncolado(admin.ModelAdmin):
	list_display = ["nick_encolado","codigo_cola"]
	class Meta:
		model = Encolado

admin.site.register(Cola, AdminCola)
admin.site.register(Encolado, AdminEncolado)
