# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0005_auto_20161030_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cola',
            name='codigo_cola',
            field=models.CharField(default='', max_length=8),
        ),
        migrations.AlterField(
            model_name='cola',
            name='nombre_cola',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='cola',
            name='propietario',
            field=models.CharField(default='', max_length=20),
        ),
    ]