# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.formats import get_format
my_formats = get_format('DATETIME_INPUT_FORMATS')
# Create your models here.

class Usuarios(models.Model):
	name = models.OneToOneField(User)
	phone = models.IntegerField()
	email = models.CharField(max_length=48)
	address= models.CharField(max_length=50)


	def __unicode__(self):
	   return '%s' % self.name

class Medicamento(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad = models.CharField(max_length=30)
    laboratorio = models.CharField(max_length=30)
    informacion = models.CharField(max_length=300)
    imagen = models.ImageField(null=True, blank=True)
    disponible = models.BooleanField(default=False)
    fecha = models.DateField(auto_now=True)
    donador = models.ForeignKey(Usuarios,on_delete=models.CASCADE)

    def __unicode__(self):
		return ("%s - %s") % (self.nombre, self.cantidad )
class Donacion(models.Model):
    beneficiario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    
    def __unicode__(self):
		return ("%s") % self.beneficiario

class Receta(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)
    doctor =  models.CharField(max_length=70)
    cedula = models.CharField(max_length=15)
    imagen = models.ImageField(null=True, blank=True)
    

    def __unicode__(self):
        return ("%s - %s") % (self.usuario, self.doctor )

