# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    rutadm = models.CharField(primary_key=True, max_length=300)
    nombreadm = models.CharField(max_length=300)
    apellidoadm = models.CharField(max_length=300)
    edadadm = models.IntegerField()
    emailadm = models.CharField(max_length=300)
    telefonoadm = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.rutadm
    class Meta:
        managed = False
        db_table = 'administrador'


class Checkin(models.Model):
    id_checkin = models.CharField(primary_key=True, max_length=300)
    cuota2 = models.IntegerField(blank=True, null=True)
    listacheck = models.CharField(max_length=300)
    reserva_rutcliente = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_rutcliente')

    class Meta:
        managed = False
        db_table = 'checkin'


class Checkout(models.Model):
    id_checkout = models.CharField(primary_key=True, max_length=300)
    listacheckout = models.CharField(max_length=300)
    multas = models.CharField(max_length=300, blank=True, null=True)
    reparaciones = models.CharField(max_length=300, blank=True, null=True)
    reserva_rutcliente = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_rutcliente')

    class Meta:
        managed = False
        db_table = 'checkout'


class Departamento(models.Model):
    id_depto = models.CharField(primary_key=True, max_length=300)
    m2 = models.CharField(max_length=300)
    piezas = models.IntegerField()
    banos = models.IntegerField()
    terraza = models.CharField(max_length=100)
    administrador_rutadm = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_rutadm')
    direccion_direccioncompleta = models.ForeignKey('Direccion', models.DO_NOTHING, db_column='direccion_direccioncompleta')
    precio = models.IntegerField()
    mantenciones_tipo_mantencion = models.ForeignKey('Mantenciones', models.DO_NOTHING, db_column='mantenciones_tipo_mantencion', blank=True, null=True)
    def __str__(self):
        return self.id_depto    

    class Meta:
        managed = False
        db_table = 'departamento'


class Direccion(models.Model):
    direccioncompleta = models.CharField(primary_key=True, max_length=300)
    region = models.CharField(max_length=300)
    comuna = models.CharField(max_length=300)
    depto = models.CharField(max_length=100)

    def __str__(self):
        return self.direccioncompleta

    class Meta:
        managed = False
        db_table = 'direccion'


class Funcionario(models.Model):
    rut_f = models.CharField(primary_key=True, max_length=300)
    nombref = models.CharField(max_length=300)
    apellidof = models.CharField(max_length=300)
    edadf = models.IntegerField()
    correof = models.CharField(max_length=300)
    telefono = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'funcionario'


class Mantenciones(models.Model):
    tipo_mantencion = models.CharField(primary_key=True, max_length=300)
    fecha = models.CharField(max_length=300)
    hora = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'mantenciones'


class Reserva(models.Model):
    rutcliente = models.CharField(primary_key=True, max_length=100)
    nombre_completo = models.CharField(max_length=100)
    fechareserva = models.CharField(max_length=300)
    cuota1 = models.IntegerField(blank=True, null=True)
    pagototal = models.IntegerField(blank=True, null=True)
    departamento_id_depto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='departamento_id_depto', blank=True, null=True)
    funcionario_rut_f = models.ForeignKey(Funcionario, models.DO_NOTHING, db_column='funcionario_rut_f', blank=True, null=True)
    correo = models.CharField(max_length=100)
    telefono = models.IntegerField()
    statusreserva = models.CharField(max_length=200,default='EN ESPERANDO PAGO RESERVA')
    servicios_extra_tipo_servicio = models.ForeignKey('ServiciosExtra', models.DO_NOTHING, db_column='servicios_extra_tipo_servicio')

    def __str__(self):
        return self.rutcliente
    @property
    def total(self):
        return (self.departamento_id_depto.precio  + self.servicios_extra_tipo_servicio.precio)
    def cuota1view(self):
        return (self.total  /2)


    class Meta:
        managed = False
        db_table = 'reserva'


class ServiciosExtra(models.Model):
    tipo_servicio = models.CharField(primary_key=True, max_length=300)
    precio = models.IntegerField()
    def __str__(self):
        return self.tipo_servicio   
    class Meta:
        managed = False
        db_table = 'servicios_extra'




