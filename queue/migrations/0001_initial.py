# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cola', models.CharField(max_length=20)),
                ('propietario', models.CharField(max_length=20)),
                ('descripcion', models.CharField(blank=True, max_length=140, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Encolado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cola', models.CharField(max_length=20)),
                ('nick', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_alta', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
