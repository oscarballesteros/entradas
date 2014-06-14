from django.conf.urls import patterns, include, url
from views import *
from django.conf import settings
urlpatterns = patterns('',
	url(r'^$',inicio),
	url(r'^nuevousuario$',nuevousuario),
	url(r'^ingresar$',ingresar),
	url(r'^regiscliente$',regiscliente),
	url(r'^clientes$',clientes),
	url(r'^index$',index),
	url(r'^index1$',inicio1),
	url(r'^index2$',inicio2),
	url(r'^reservass$',reservass),
	url(r'^clientesregis$',clientesregis),
	url(r'^galeria$',galeria),
	url(r'^sectors$',sectors),
	url(r'^preferencias$',preferencias),
	url(r'^reservas$',reservacion),
	url(r'^partidos$',partidos),
	url(r'^paypal$',paypal),



	)