# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Tabla auxiliar Planes por Afiliado
class TbafiliadosPlanes(models.Model):
    registroid = models.AutoField(db_column='RegistroID', primary_key=True)  # Field name made lowercase.
    afiliadodni = models.IntegerField(db_column='AfiliadoDNI')  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanID')  # Field name made lowercase.
    afiliadonumplan = models.CharField(db_column='AfiliadoNumPlan', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbafiliados_planes'

# Tabla auxiliar Redes Sociales por afiliado
class TbafiliadosRedessociales(models.Model):
    afiliadodni = models.IntegerField(db_column='AfiliadoDNI', primary_key=True)  # Field name made lowercase.
    redid = models.IntegerField(db_column='RedID')  # Field name made lowercase.
    redusuario = models.CharField(db_column='RedUsuario', max_length=50)  # Field name made lowercase.
    comentario = models.TextField(db_column='Comentario')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbafiliados_redessociales'

# Tabla maestra de Atención a la mascota
class TbatencionDetalle(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    afidni = models.IntegerField(db_column='afiDNI')  # Field name made lowercase.
    mascotaid = models.IntegerField(db_column='MascotaID')  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanID')  # Field name made lowercase.
    especialidadid = models.IntegerField(db_column='EspecialidadID')  # Field name made lowercase.
    servicioid = models.CharField(db_column='ServicioID', max_length=3)  # Field name made lowercase.
    estadoservicio = models.CharField(db_column='EstadoServicio', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbatencion_detalle'

# Tabla maestra de diagnósticos
class TbatencionDiagnosticos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mascotaid = models.IntegerField(db_column='MascotaID')  # Field name made lowercase.
    servicioid = models.CharField(db_column='ServicioID', max_length=3)  # Field name made lowercase.
    chequeo = models.TextField(db_column='Chequeo')  # Field name made lowercase.
    diagnostico = models.TextField(db_column='Diagnostico')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbatencion_diagnosticos'


class TbatencionHead(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    vet_user = models.CharField(max_length=50)
    afidni = models.IntegerField(db_column='afiDNI')  # Field name made lowercase.
    mascotaid = models.IntegerField(db_column='MascotaID')  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbatencion_head'


class TbcalendarioPagos(models.Model):
    fecha = models.DateField(db_column='Fecha', unique=True, blank=True, null=True)  # Field name made lowercase.
    dia = models.IntegerField()
    mes = models.IntegerField()
    quarter = models.IntegerField()
    anio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbcalendario_pagos'


class TbespecialidadRegistro(models.Model):
    espid = models.IntegerField(db_column='EspID', primary_key=True)  # Field name made lowercase.
    descespecialidad = models.CharField(db_column='DescEspecialidad', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbespecialidad_registro'


class TbespecialidadServicio(models.Model):
    srvid = models.AutoField(db_column='srvID', primary_key=True)  # Field name made lowercase.
    descservicio = models.CharField(db_column='DescServicio', max_length=150, blank=True, null=True)  # Field name made lowercase.
    espid = models.IntegerField(db_column='EspID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbespecialidad_servicio'



class TbmascotasSexo(models.Model):
    sexoid = models.AutoField(db_column='SexoID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbmascotas_sexo'


class TbpagosAfiliados(models.Model):
    pagoid = models.IntegerField(db_column='PagoID', primary_key=True)  # Field name made lowercase.
    afiliadodni = models.IntegerField(db_column='AfiliadoDNI', blank=True, null=True)  # Field name made lowercase.
    pagovencimiento = models.DateField(db_column='PagoVencimiento', blank=True, null=True)  # Field name made lowercase.
    pagofecha = models.DateField(db_column='PagoFecha', blank=True, null=True)  # Field name made lowercase.
    pagoimporte = models.IntegerField(db_column='PagoImporte', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbpagos_afiliados'





class TbplanesServicios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanID')  # Field name made lowercase.
    espid = models.IntegerField(db_column='EspID')  # Field name made lowercase.
    servid = models.CharField(db_column='ServID', max_length=3)  # Field name made lowercase.
    fechaalta = models.DateField(db_column='FechaAlta')  # Field name made lowercase.
    fechahasta = models.DateField(db_column='FechaHasta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbplanes_servicios'


class TbplanesVigPrecios(models.Model):
    planid = models.IntegerField(db_column='PlanID', primary_key=True)  # Field name made lowercase.
    fechainicial = models.DateField(db_column='FechaInicial', blank=True, null=True)  # Field name made lowercase.
    fechafinal = models.DateField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    precio = models.IntegerField(db_column='Precio', blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbplanes_vig_precios'


class TbproductosRegistro(models.Model):
    medid = models.CharField(db_column='medID', primary_key=True, max_length=11)  # Field name made lowercase.
    medidsecundario = models.CharField(db_column='medIDSecundario', max_length=4)  # Field name made lowercase.
    medtipoid = models.CharField(db_column='medTipoID', max_length=2)  # Field name made lowercase.
    meddenominacion = models.CharField(db_column='medDenominacion', max_length=100)  # Field name made lowercase.
    medidprov = models.CharField(db_column='medIDProv', max_length=4)  # Field name made lowercase.
    medprecio = models.DecimalField(db_column='medPrecio', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbproductos_registro'




class Tbusuarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    user_img = models.TextField(blank=True, null=True)
    groupid = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    ext_security_id = models.CharField(max_length=100, blank=True, null=True)
    login_session_key = models.CharField(max_length=255, blank=True, null=True)
    email_status = models.CharField(max_length=255, blank=True, null=True)
    password_expire_date = models.DateTimeField(blank=True, null=True)
    password_reset_key = models.CharField(max_length=255, blank=True, null=True)
    account_status = models.CharField(max_length=255, blank=True, null=True)
    reset_token = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbusuarios'


class TbvetEspecialidad(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    vetid = models.IntegerField(db_column='vetID', blank=True, null=True)  # Field name made lowercase.
    espid = models.IntegerField(db_column='espID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbvet_especialidad'


class TbveterinariaServicio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    vetid = models.IntegerField(db_column='vetID')  # Field name made lowercase.
    espid = models.IntegerField(db_column='espID')  # Field name made lowercase.
    srvid = models.CharField(db_column='srvID', max_length=3)  # Field name made lowercase.
    vigencia = models.CharField(max_length=10)
    costovet = models.DecimalField(db_column='CostoVet', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbveterinaria_servicio'


class TbveterinariasAgenda(models.Model):
    agdregid = models.IntegerField(db_column='agdRegID', primary_key=True)  # Field name made lowercase.
    agdveterinariaid = models.IntegerField(db_column='agdVeterinariaID')  # Field name made lowercase.
    agddia = models.CharField(db_column='agdDia', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbveterinarias_agenda'


