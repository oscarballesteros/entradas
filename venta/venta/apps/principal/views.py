from django.shortcuts import render, render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from forms import *
from models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from venta.settings import RUTA_PROYECTO
import pdb
#import datetime
# Create your views here.
def inicio(request):
	emple=empleado.objects.all()
	return render_to_response('index.html',{'emple':emple},RequestContext(request))
def inicio1(request):
	
	return render_to_response('index1.html',{},RequestContext(request))
def inicio2(request):
	
	return render_to_response('index2.html',{},RequestContext(request))
def reservass(request):
	
	return render_to_response('reservass.html',{},RequestContext(request))
def nuevousuario(request):
	if request.method=='POST':
		formulario=UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/index')
	else:
		formulario=UserCreationForm()
	return render_to_response('regisusuario.html',{'formulario':formulario},context_instance=RequestContext(request))
def ingresar(request):
	if request.method=='POST':
		formulario=AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario=request.POST['username']
			clave=request.POST['password']
			acceso=authenticate(username=usuario,password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request,acceso)
					return HttpResponseRedirect('/index2')
				else:
					return render_to_response('noactivo.html',context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html',context_instance=RequestContext(request))
	else:
		formulario=AuthenticationForm()
	return render_to_response('ingresar.html',{'formulario':formulario},context_instance=RequestContext(request))
@login_required(login_url='/ingresar')
def index(request):
	return render_to_response('index.html',{},RequestContext(request))
#@login_required(login_url='/ingresar')

def regiscliente(request):
	if request.method=='POST':
		formu=clienteform(request.POST)
		if formu.is_valid():
			formu.save()
			return HttpResponseRedirect('/clientes')
	else:
		formu=clienteform()

	#return render_to_response('clientereg.html',{},context_instance=RequestContext(request))
	return render_to_response('regiscliente.html',{'formu':formu},context_instance=RequestContext(request))
@login_required(login_url='/ingresar')
def clientes(request):
	client=cliente.objects.all()
	return render_to_response('clientereg.html',{},context_instance=RequestContext(request))
	#return render_to_response('client.html',{'client':client},context_instance=RequestContext(request))

def clientesregis(request):
	datos=cliente.objects.all()
	return render_to_response('client.html',{'datos':datos},context_instance=RequestContext(request))

#def hola(request):
#	return render_to_response("index.html",{"fecha":datetime.datetime.today()})
def galeria(request):
	return render_to_response('galeria.html',{},RequestContext(request))

def sectors(request):
	return render_to_response('sectores.html',{},RequestContext(request))

def preferencias(request):
	res=get_object_or_404(asientos,fila="12")
	#asi=asientos.objects.all()
	#pos=500
	##pdb.set_trace()
	return render_to_response('preferencia.html',{'res':res},RequestContext(request))
def reservacion(request):
	if request.method=='POST':
		formulario=reservaform(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=reservaform()

	return render_to_response('reserva.html',{'formu':formulario},RequestContext(request))

def partidos(request):
	par=encuentros.objects.all()
	return render_to_response('partidos.html',{'par':par},RequestContext(request))

def paylpas(request):
	if request.method=='POST':
		formulario=paypalform(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario=paypalform()

	return render_to_response('`pago.html',{'formu':formulario},RequestContext(request))
