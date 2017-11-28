# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Usuarios, Medicamento, Donacion,Receta
# Register your models here.
admin.site.register(Medicamento)
admin.site.register(Donacion)
admin.site.register(Usuarios)
admin.site.register(Receta)
