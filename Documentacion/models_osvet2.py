# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# Tabla maestra de Afiliados
class Afiliado(models.Model):
    fechaalta = models.DateField(db_column='FechaAlta')  # Field name made lowercase.
    zonaid = models.IntegerField(db_column='ZonaID')  # Field name made lowercase.
    dniid = models.IntegerField(db_column='DNIID')  # Field name made lowercase. CHOICE
    afiliadodni = models.IntegerField(db_column='AfiliadoDNI')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=255)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=25)  # Field name made lowercase.
    foto = models.TextField()
    estado = models.CharField(db_column='Estado', max_length=20, blank=True, null=True)  # Field name made lowercase. CHOICE
    report = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tbafiliados_registro'

# Tabla maestra de Mascotas
class Mascota(models.Model):
    # mascotaid = models.AutoField(db_column='MascotaID', primary_key=True)  # Field name made lowercase.
    afiliadodni = models.IntegerField(db_column='AfiliadoDNI')  # Field name made lowercase.
    fechaalta = models.DateField(db_column='FechaAlta')  # Field name made lowercase.
    fechanac = models.DateField(db_column='FechaNac')  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    especie = models.IntegerField(db_column='Especie')  # Field name made lowercase.
    razaid = models.IntegerField(db_column='RazaID')  # Field name made lowercase.
    sexo = models.IntegerField(db_column='Sexo')  # Field name made lowercase. CHOICE
    pelaje = models.CharField(db_column='Pelaje', max_length=15)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=15)  # Field name made lowercase.
    tamanio = models.CharField(db_column='Tamanio', max_length=15)  # Field name made lowercase. CHOICE
    foto = models.TextField(db_column='Foto')  # Field name made lowercase.
    planid = models.IntegerField(db_column='PlanID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbafiliados_mascotas'

#Tabla maestra de especies
class Especies(models.Model):
    denominacion = models.CharField(db_column='Denominacion', max_length=50)  # Field name made lowercase.
    imagen = models.ImageField(("icono"), upload_to='pet/', height_field=None, width_field=None, max_length=None)

    class Meta:
        managed = False
        db_table = 'Pet_Species'

# Tabla maestra de Planes/Coberturas
class Planes(models.Model):
    # planid = models.IntegerField(db_column='PlanID', primary_key=True)  # Field name made lowercase.
    denominacion = models.CharField(db_column='Denominacion', max_length=15, blank=True, null=True)  # Field name made lowercase.
    cupomax = models.IntegerField(db_column='CupoMax', blank=True, null=True)  # Field name made lowercase.
    vigencia = models.IntegerField(db_column='Vigencia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbplanes_registro'

# Tabla maestra de Proveedores
class Proveedores(models.Model):
    # proveedorid = models.CharField(db_column='ProveedorID', primary_key=True, max_length=4)  # Field name made lowercase.
    razonsocial = models.CharField(db_column='RazonSocial', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbproveedores_registro'

# Tabla maestra de Razas de mascotas
class Razas(models.Model):
    # razaid = models.AutoField(db_column='RazaID', primary_key=True)  # Field name made lowercase.
    denominacion = models.CharField(db_column='Denominacion', max_length=50)  # Field name made lowercase.
    foto = models.TextField(db_column='Foto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbrazas_registro'

# Tabla maestra de servicios
class Servicios(models.Model):
    # srvid = models.CharField(db_column='srvID', primary_key=True, max_length=3)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbservicios_registro'

# Tabla maestra de Veterinarias
class Veterinarias(models.Model):
    # veterinariaid = models.AutoField(db_column='VeterinariaID', primary_key=True)  # Field name made lowercase.
    fechaalta = models.DateField(db_column='FechaAlta', blank=True, null=True)  # Field name made lowercase.
    denominacion = models.CharField(db_column='Denominacion', max_length=25, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=25, blank=True, null=True)  # Field name made lowercase.
    responsable = models.CharField(db_column='Responsable', max_length=25, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=25, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=15, blank=True, null=True)  # Field name made lowercase.
    telefonourgencias = models.CharField(db_column='TelefonoUrgencias', max_length=15, blank=True, null=True)  # Field name made lowercase.
    zonaid = models.IntegerField(db_column='zonaID', blank=True, null=True)  # Field name made lowercase.
    campo2 = models.CharField(db_column='Campo2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    campo3 = models.CharField(db_column='Campo3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    campo4 = models.CharField(db_column='Campo4', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbveterinarias_registro'

# Tabla maestra de Zonas
class Zonas(models.Model):
    # zonaid = models.AutoField(db_column='zonaID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbzonas_registro'
