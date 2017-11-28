# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import FormView
from .forms import Users_Form,medform,donform,recetform
from django.core.urlresolvers import reverse_lazy
from .models import Usuarios,Medicamento,Donacion,Receta
from django.db import IntegrityError
from django.shortcuts import render_to_response
from django.db import IntegrityError
from  django.http import HttpResponse
from django.views.generic import DetailView,UpdateView

# Create your views here.

#validar campos
class Signup(FormView):
	template_name= 'signup.html'
	form_class = Users_Form
	success_url = reverse_lazy('login')

	def form_valid(self, form):
		user = form.save()
		p = Usuarios()
		p.name = user
		p.phone = form.cleaned_data['phone']
		p.email = form.cleaned_data['email']
		p.address = form.cleaned_data['address']

		p.save()
		return super(Signup, self).form_valid(form)



def medview(request):
	form = medform(request.POST or None, request.FILES or None)
	p = Medicamento()
	if form.is_valid():
		nombre = form.cleaned_data["nombre"]
		cantidad = form.cleaned_data["cantidad"]
		laboratorio = form.cleaned_data["laboratorio"]
		informacion = form.cleaned_data["informacion"]
		donador = form.cleaned_data["donador"]
		imagen =  form.cleaned_data["imagen"]


		p.nombre = nombre
		p.cantidad = cantidad
		p.laboratorio = laboratorio
		p.informacion = informacion
		p.imagen = imagen
		p.donador = donador
	
		p.save()

		form = medform()

	return render(request, 'medicamento.html',{"form":form} )

def donview(request):
	form = donform(request.POST or None)
	p = Donacion()
	if form.is_valid():
		
		beneficiario = form.cleaned_data["beneficiario"]
		
		medicamento = form.cleaned_data["medicamento"]
			
		p.beneficiario = beneficiario
		p.medicamento = medicamento
		
		
		p.save()

		t1 = Medicamento.objects.all()
		for x in t1:
			if x==medicamento:
				x.disponible=True
				x.save()

				  
		
		form = donform()

	return render(request, 'donacion.html',{"form":form} )

def usuariosview(request):
		usuarios = Usuarios.objects.all()
		contexto = {'usuarios':usuarios}


		return render(request,'usuarios.html',contexto)

def impmedicamento(request):
	medicamentos = Medicamento.objects.all()
	contexto = {'medicamentos':medicamentos}

	return render(request,'mostrarmedicamentos.html',contexto)
class updtmed(UpdateView):
	template_name = "updatemed.html"
	model = Medicamento
	fields = "__all__"
	success_url = reverse_lazy(impmedicamento)


class dmedicamento(DetailView):
	template_name = "detallemedicamento.html"
	model = Medicamento

def recetaview(request):
	form=recetform(request.POST or None, request.FILES or None)
	p=Receta()
	if form.is_valid():
		usuario=form.cleaned_data["usuario"]
		imagen=form.cleaned_data["imagen"]
		doctor=form.cleaned_data["doctor"]
		cedula=form.cleaned_data["cedula"]

		p.usuario = usuario
		p.imagen = imagen
		p.doctor = doctor
		p.cedula = cedula

		p.save()

		form=recetform()

	return render(request,'receta.html',{"form":form})

def impdonaciones(request):
	donaciones = Donacion.objects.all()
	contexto = {'donaciones':donaciones}

	return render(request,'mostrardonaciones.html',contexto)
class detdonac(DetailView):
	template_name = "detalledonaciones.html"
	model = Donacion
	

	

def imprecetas(request):
	recetas = Receta.objects.all()
	contexto = {'recetas':recetas}

	return render(request,'mostrarrecetas.html',contexto)
class detrecetas(DetailView):
	template_name = "detallerecetas.html"
	model = Receta

def farmaciav(request):
		return render(request,'farmacia.html')


def consultoriov(request):
		return render(request,'consultorio.html')

def casa(request):

	#total de medicamementos
	rw1 = Medicamento.objects.all().count()
	#total de medicamentos disponibles
	rw2 =  Medicamento.objects.filter(disponible=0).count()
	#total de donaciones relizadas
	rw3 = Donacion.objects.count()
	#usuarios beneficiarios
	rw4 = Usuarios.objects.count()

	return render(request,"casa.html",{"rw1":rw1,"rw2":rw2,"rw3":rw3,"rw4":rw4})
def login(request):
	
		return render(request,'login.html')
