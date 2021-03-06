# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('queue', '0006_auto_20161030_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cola',
            name='id',
        ),
        migrations.AddField(
            model_name='cola',
            name='integrantes',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='cola',
            name='codigo_cola',
            field=models.CharField(default='', max_length=8, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='encolado',
            name='codigo_cola',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='queue.Cola'),
        ),
    ]
