from django.contrib import admin
from .models import Departamento,Administrador,Direccion,Reserva,Funcionario,  ServiciosExtra, Mantenciones
# Register your models here.

admin.site.register(Departamento)
admin.site.register(Administrador)
admin.site.register(Direccion)
admin.site.register(Reserva)
admin.site.register(Funcionario)
admin.site.register(ServiciosExtra)
admin.site.register(Mantenciones)

admin.site.site_header = "ArriendosTemporada Administracion"
admin.site.site_title = "ArriendosTemporada Administracion"
admin.site.index_title = "Bienvenid@ a la vista de Funcionario - ArriendosTemporada"