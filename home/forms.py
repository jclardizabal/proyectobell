from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Medicamento,Usuarios
class Users_Form(UserCreationForm):
	phone = forms.IntegerField()
	email = forms.CharField(max_length=48)
	address = forms.CharField(max_length=256)


class medform(forms.Form):
	donador = forms.ModelChoiceField(queryset=Usuarios.objects.all())
	nombre = forms.CharField(max_length=48)
	cantidad = forms.CharField(max_length=48)
	laboratorio =forms.CharField()
	imagen =  forms.ImageField(None)
	informacion = forms.CharField(max_length=300)


class donform(forms.Form):
	beneficiario = forms.ModelChoiceField(queryset=Usuarios.objects.all())
	medicamento = forms.ModelChoiceField(queryset=Medicamento.objects.filter(disponible=False))

class recetform(forms.Form):
	usuario=forms.ModelChoiceField(queryset=Usuarios.objects.all())
	doctor = forms.CharField(max_length=70)
	cedula = forms.CharField(max_length=15)
	imagen =  forms.ImageField(None)

