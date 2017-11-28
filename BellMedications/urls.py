"""BellMedications URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home import views
from django.contrib.auth.views import login, logout_then_login
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'^login/$',login,{'template_name': 'login.html'},name='login'),
	url(r'^cerrar/$', logout_then_login, name='logout'),
	url(r'^signup/$', views.Signup.as_view() ,name='signup'),
	url(r'^$', views.casa, name="casa_view"),
	url(r'^registrarmedicamento/$', views.medview ,name='registrarmedicamento_view'),
	url(r'^donacion/$', views.donview ,name='donacion_view'),
	url(r'^usuarios/$', views.usuariosview ,name='usuarios_view'),
	url(r'^receta/$', views.recetaview,name="receta_view"),
	url(r'^farmacia/$', views.farmaciav,name="farmacia_view"),
	
	url(r'^consultorio/$', views.consultoriov,name="consultorio_view"),

	url(r'^mostrar_medicamentos/$', views.impmedicamento,name="medicamentos_view"),
	url(r'detalle_medicamento/(?P<pk>\d+)/$',views.dmedicamento.as_view(),name='detail_medicamento_view'),
	url(r'actualizar_medicamento/(?P<pk>[-\d]+)/$',views.updtmed.as_view(),name='update_med_view'),

	url(r'^mostrar_donaciones/$', views.impdonaciones,name="donaciones_view"),
	url(r'detalle_donacion/(?P<pk>\d+)/$',views.detdonac.as_view(),name='detail_medicamento_view'),

	url(r'^mostrar_recetas/$', views.imprecetas,name="recetas_view"),
	url(r'detalle_receta/(?P<pk>\d+)/$',views.detrecetas.as_view(),name='detail_recetas_view'),
	

]
if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)