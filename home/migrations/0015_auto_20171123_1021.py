# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 10:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20171123_1018'),
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
