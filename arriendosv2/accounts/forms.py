from django import forms 
from django.forms import ModelForm
from .models import Departamento,Reserva,Transporte




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
        "servicios_extra_tipo_servicio":"Desea Servicio Extra?"
   		}
		widgets = {	
					'rutcliente': forms.TextInput(attrs={'class':'form-control'}),
					'nombre_completo': forms.TextInput(attrs={'class':'form-control'}),
					'fechareserva':forms.DateInput(format=("%Y-%m-%d"),attrs={'class': 'form-control', 
               'placeholder': 'Select a date','type': 'date'}),
					'correo': forms.EmailInput(attrs={'class':'form-control'}),
					'telefono': forms.TextInput(attrs={'class':'form-control'}),
					'departamento_id_depto':forms.Select(attrs={'class': 'form-control'}),
					'servicios_extra_tipo_servicio':forms.Select(attrs={'class': 'form-control'}),
					
			}

   	
class PlanificacionForm(ModelForm):
	class Meta:
		model =Transporte
		fields = 'desde','horario','reserva_rutcliente'
		labels = {
        "desde": "Direccion donde te buscaremos",
        "horario": "Hora la cual deseas ser recogido",
        "reserva_rutcliente":"Rut Reserva",
   		}
		widgets = {	
					'reserva_rutcliente': forms.TextInput(attrs={'class':'form-control'}),
					'desde': forms.TextInput(attrs={'class':'form-control'}),
					'horario': forms.TextInput(attrs={'class':'form-control'}),
				
					
			}

 