# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_receta'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicamento',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]
