# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 10:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_medicamento_fechayhora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicamento',
            name='fechayhora',
        ),
        migrations.RemoveField(
            model_name='medicamento',
            name='hora',
        ),
    ]
