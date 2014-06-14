from django.db import models

# Create your models here.
class empleado(models.Model):
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	ci=models.IntegerField(unique=True)
	direccion=models.CharField(max_length=200)
	telefono=models.IntegerField(max_length=20)
	email=models.EmailField(max_length=50)
	cargo=models.CharField(max_length=200)
	fecha=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "%s "%(self.nombre)

class cliente(models.Model):
	ci=models.CharField(max_length=20)
	nombre=models.CharField(max_length=200)
	apellido=models.CharField(max_length=200)
	telefono=models.IntegerField(max_length=20)
	email=models.EmailField(max_length=75)
	direccion=models.CharField(max_length=200)
	fecha=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.nombre
torneos = (
   ('liga boliviana', 'Liga boliviana'),
   ('libertadores', 'Libertadores'),
   ('sudamericana', 'Sudamericana'),
)
class encuentros(models.Model):
	torneo=models.CharField(max_length=50,choices=torneos)
	equipo1=models.CharField(max_length=50)
	equipo2=models.CharField(max_length=50)
	fecha=models.DateField()
	hora=models.TimeField()	
	curvaN = models.IntegerField()
	curvaS = models.IntegerField()
	general = models.IntegerField()
	preferencia= models.IntegerField()
	def __unicode__(self):
		return "%s vs %s"%(self.equipo1,self.equipo2)

estados = (

   ('disponible', 'Disponible'),
   ('reservado', 'Reservado'),
   ('vendido', 'Vendido'), 
)
class asientos(models.Model):
	estado=models.CharField(max_length=50,choices=estados)
	fila=models.CharField(max_length=10)
	numeroasietos=models.CharField(max_length=10)
	def __unicode__(self):
		return "%s %s"%(self.estado,self.fila)


class reservas(models.Model):
	idencuentros=models.ForeignKey(encuentros)
	idasiento=models.ForeignKey(asientos)
	sector=models.CharField(max_length=50)
	Nombre=models.CharField(max_length=200)
	Apellido=models.CharField(max_length=200)
	CI=models.CharField(max_length=10)
	telefono=models.IntegerField(max_length=200)
	fecha=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "%s %s"%(self.Nombre,self.idencuentros)

class factura(models.Model):
	idreserva=models.ForeignKey(reservas)
	total=models.FloatField()
	descripcion=models.CharField(max_length=200)
	fecha=models.DateTimeField(auto_now=True)

class galeria(models.Model):
	nombre=models.CharField(max_length=200)
	fotografia=models.ImageField(upload_to='venta/carga')
	def __unicode__(self):
		return "%s "%(self.nombre)

tarjetas = (

   ('visa', 'Visa'),
   ('mastercard', 'Mastercard'),
   ('bnb', 'BnB'),
   ('bancounion', 'BancoUnion'),
   ('bcp', 'BCP'),  
)

class paypal(models.Model):
	pais=models.CharField(max_length=20)
	tarjeta=models.CharField(max_length=50,choices=tarjetas)
	Numero_de_tarjeta=models.CharField(max_length=20)
	fecha_vencimiento=models.DateField()
	codigo_seg=models.IntegerField()
	def __unicode__(self):
		return "%s"%(self.pais)


