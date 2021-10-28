from django import forms 
from django.forms import ModelForm
from .models import Departamento,Reserva




#create a venue form



class ReservaForm(ModelForm):
	class Meta:
		model = Reserva
		fields = 'rutcliente','nombre_completo','fechareserva','departamento_id_depto','correo','telefono','servicios_extra_tipo_servicio'
		labels = {
        "rutcliente": "Rut",
        "nombre_completo": "Nombre Completo",
        "fechareserva":"Fecha para reservar",
        "departamento_id_depto": "ID Departamento que desea:",
        "servicios_extra_tipo_servicio":"¿Desea Servicio Extra?"
   		}
		widgets = {	
					'rutcliente': forms.TextInput(attrs={'class':'form-control'}),
					'nombre_completo': forms.TextInput(attrs={'class':'form-control'}),
					'fechareserva':forms.DateInput(attrs={'class':'form-control'}),
					'correo': forms.EmailInput(attrs={'class':'form-control'}),
					'telefono': forms.TextInput(attrs={'class':'form-control'}),
					
			}

   	

   	 

 