from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.db import connection
from django.template import Context, loader
from .models import Departamento,Reserva,Transporte,Checkout
from.forms import ReservaForm, PlanificacionForm
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
import datetime




#PDF
import io 
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

#generar pdf
def venue_pdf(request,searched):
	#crear yte
	buf = io.BytesIO()
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	textob=c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica",14)
	#texto
	#modelo
	IDCAPT = Reserva.objects.get(rutcliente__exact=searched)
	CHECKIN1 = Reserva.objects.filter(rutcliente__exact=IDCAPT)
	
	lines = []

	for reserva in CHECKIN1:
		lines.append("==================================")
		lines.append('RUT RESERVA:')
		lines.append(reserva.rutcliente)
		lines.append("INVENTARIO COCINA:")
		lines.append(reserva.departamento_id_depto.inventario_id_inv.cocina)
		lines.append("INVENTARIO MUEBLES:")
		lines.append(reserva.departamento_id_depto.inventario_id_inv.muebles)
		lines.append("INVENTARIO BANO:")
		lines.append(reserva.departamento_id_depto.inventario_id_inv.banoinv)
		lines.append("INVENTARIO CAMAS:")
		lines.append(reserva.departamento_id_depto.inventario_id_inv.camas)
		lines.append("INVENTARIO EXTRAS:")
		lines.append(reserva.departamento_id_depto.inventario_id_inv.extras)
		lines.append("==================================")
		lines.append("PAGO CHECKIN:")
		lines.append(str(reserva.cuota1))
		lines.append("TOTAL PAGADO (CHECKIN + RESERVA):")
		lines.append(str(reserva.total))
		lines.append("==================================")


	




	for line in lines:
		textob.textLine(line)



	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	return FileResponse(buf, as_attachment=True,filename="venue.pdf")




from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
	return render(request,'accounts/dashboard.html')

def propiedades (request):
	departamentos_lista = Departamento.objects.all()
	return render(request,'accounts/propiedades.html',
		{'departamentos_lista':departamentos_lista})






def checkin (request, searched):
	if Reserva.objects.filter(rutcliente__exact=searched).exists():
		t=Reserva.objects.get(rutcliente__exact=searched)
		
		if t.statusreserva=="RESERVA COMPLETADA":
			messages.error(request,'Esta reserva ya esta pagada')
			return redirect(request.META['HTTP_REFERER'])

		else:
			IDCAPT = Reserva.objects.get(rutcliente__exact=searched)
			CHECKIN1 = Reserva.objects.filter(rutcliente__exact=IDCAPT)
			return render (request,'accounts/checkin.html',{'IDCAPT':IDCAPT,'CHECKIN1':CHECKIN1,})
	else:
		
		return render (request,'accounts/checkin.html',)


@login_required(login_url='loginpage')
def checkout (request):
	return render(request,'accounts/checkout.html')


@login_required(login_url='loginpage')
def adminapp (request):
	return render(request,'accounts/adminapp.html')



def loginpage (request):
	if request.user.is_authenticated:
			return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.success (request,'Usuario o contrase??a incorrectos')


  	
	return render(request,'accounts/login.html')


def reserva(request):
	departamentos_lista = Departamento.objects.all()
	submitted=False
	if request.method == "POST":
		form = ReservaForm(request.POST)
		
		if form.is_valid():
			
			form.save()
			messages.success (request,'Se genero tu solicitud de reserva con exito!')
			return HttpResponseRedirect('/reserva?submitted=true')
	else:
		form = ReservaForm
		
		if 'submitted' in request.GET:
			submitted= True

	return render(request,'accounts/reserva.html',
		{'departamentos_lista':departamentos_lista,'form':form, 'submitted':submitted})




def busqueda_reserva (request):
	
	if request.method == "POST":
		searched = request.POST['searched']
		reservas = Reserva.objects.filter(rutcliente__exact=searched)
		transportes = Transporte.objects.filter(reserva_rutcliente=searched)
		checkouts = Checkout.objects.filter(reserva_rutcliente=searched)
		

		return render(request,'accounts/busqueda.html',{'searched':searched,'reservas':reservas,'transportes':transportes,'checkouts':checkouts})

	else:
		return render(request,'accounts/busqueda.html')

	

def delete_reserva (request, searched):
	reserva = Reserva.objects.get(rutcliente__exact=searched)
	reserva.delete()
	messages.success(request,'Reserva eliminada con exito')
	return render(request,'accounts/busqueda.html')




def pago (request,searched):

	if Reserva.objects.filter(rutcliente__exact=searched).exists():
		t=Reserva.objects.get(rutcliente__exact=searched)
		
		if t.statusreserva=="RESERVA REALIZADA - PAGADA":
			messages.error(request,'Esta reserva ya esta pagada')
			return redirect(request.META['HTTP_REFERER'])

		else:
			IDCAPT = Reserva.objects.get(rutcliente__exact=searched)
			PAGO = Reserva.objects.filter(rutcliente__exact=IDCAPT)
			return render (request,'accounts/pago.html',{'IDCAPT':IDCAPT,'PAGO':PAGO,})
	else:
		
		return render (request,'accounts/pago.html',)
	




def agregar_pago (request,searched):
	t=Reserva.objects.get(rutcliente__exact=searched)
	t.cuota1= t.cuota1view()
	t.statusreserva = "RESERVA REALIZADA - PAGADA"
	t.save()
	messages.success(request,'Tu Reserva se pago con exito')
	return render(request,'accounts/busqueda.html')

def agregar_checkin (request,searched):
	t=Reserva.objects.get(rutcliente__exact=searched)
	t.pagototal= t.cuota1view()
	t.statusreserva = "RESERVA COMPLETADA"
	t.save()
	messages.success(request,'Tu Checkin se pago con exito')
	return render(request,'accounts/busqueda.html')




def planificar(request):
	reservas_lista = Reserva.objects.all()
	submitted=False
	if request.method == "POST":
		form = PlanificacionForm(request.POST)
		
		if form.is_valid():
			
			form.save()
			messages.success (request,'Se planifico tu transporte con exito!')
			return HttpResponseRedirect('/planificar?submitted=true')
	else:
		
		form = PlanificacionForm
		
		if 'submitted' in request.GET:
			submitted= True

	return render(request,'accounts/planificar.html',
		{'reservas_lista':reservas_lista,'form':form, 'submitted':submitted})



