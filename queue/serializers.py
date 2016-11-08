from rest_framework import serializers
from .models import Cola

class ColaSerializer(serializers.Serializer):
	codigo_cola = serializers.CharField(default='',max_length=8, allow_blank=False, allow_null=False)
	propietario = serializers.CharField(default='',max_length=20, allow_blank=False, allow_null=False)
	nombre_cola = serializers.CharField(default='',max_length=20, allow_blank=False, allow_null=False)
	descripcion = serializers.CharField(max_length=140, allow_blank=True, allow_null=True)
	integrantes = serializers.IntegerField(default=0, allow_null=False)

	def create(self, validated_data):
		return Cola.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.codigo_cola=validated_data.get('codigo_cola', instance.codigo_cola)
		instance.propietario=validated_data.get('propietario', instance.propietario)
		instance.nombre_cola=validated_data.get('nombre_cola', instance.nombre_cola)
		instance.descripcion=validated_data.get('descripcion', instance.descripcion)
		instance.integrantes=validated_data.get('integrantes', instance.integrantes)

		instance.save()
		return instance
