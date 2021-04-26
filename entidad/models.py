from django.db import models

class Localidad(models.Model):
    nombre_l = models.CharField(max_length=50)
    cp = models.CharField("Código Postal",max_length=50)
    provincia = models.CharField(max_length=50)
    fecha_carga = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Localidades"

    def __str__(self):
        return '%s , %s' % (self.cp, self.nombre_l) 

class Persona(models.Model):
    objects = None
    nombre= models.CharField("Nombre/s", max_length=150)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField(null=True, blank=True)
    fecha_nac = models.DateField("Fecha de Nacimiento")
    calle = models.CharField(max_length=100, null=True, blank=True)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    fecha_carga = models.DateTimeField(null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '%s, %s' % (self.apellido, self.nombre)

class Categoria(models.Model):
    nombre = models.CharField(max_length=70, verbose_name='Categoria')
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre

class Unidad_medida(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Unidad de medida')
    fecha_carga = models.DateTimeField()
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    #subclase meta para aclarar como se ve la clase en plural
    class Meta:
        verbose_name_plural = "Unidades de medida"

    def __str__(self):
        return self.nombre


class Articulo(models.Model):
    codigo = models.CharField(max_length=150, null=True, unique=True, verbose_name='codigo')
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripcion')
    cantidad = models.TextField(max_length =5, null=True, blank=True)
    unidad_de_medida = models.ForeignKey(Unidad_medida, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    precio_lista = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)                                       
    descuento = models.DecimalField(max_digits=10, decimal_places=3, default=0, null=True, blank=True)                                
    aumento = models.DecimalField(max_digits=10, decimal_places=3, default=0, null=True, blank=True)                                  
    iva = models.DecimalField(max_digits=10, decimal_places=3, default=0, null=True, blank=True)
    flete = models.DecimalField(max_digits=10, decimal_places=3, default=0, null=True, blank=True)
    ganancia = models.DecimalField(max_digits=10, decimal_places=3, default=0, null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to="images/")
                                   
    #es muy util poner usuario que realiza la carga y actualizacion

    def __str__(self):
        return '%s, %s' % (self.nombre, self.descripcion)

class TipoMovimiento(models.Model):
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10, null=True, blank=True)
    autonumerico = models.BooleanField(default=True)
    fecha_carga = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

#esta clase es de las ventas pero le pongo movimiento
class Movimiento(models.Model):
    tipo = models.ForeignKey(TipoMovimiento , verbose_name="Tipo de movimiento", help_text="Tipo de movimiento", on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha", help_text="Fecha de carga")
    numero1 = models.CharField(max_length=5, default='00001', help_text="Numero")
    numero = models.CharField(max_length=15)
    cliente = models.ForeignKey(Persona, limit_choices_to={'activo': True}, default='1', 
                                help_text="N° de documento o CUIT del tercero", on_delete=models.CASCADE)
    sutbtotal = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    #en articulo on_delete cascade permite que no se borre un movimiento si se borra el articulo
    articulo = models.ForeignKey(Articulo, related_name='Articulo', null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_carga = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '%s %s %s' % (self.numero1, self.numero, self.tipo)

class Pais(models.Model):
    nombre_p = models.CharField("Nombre del pais", max_length=150)

    class Meta:
        verbose_name_plural = "Paises"
    def __str__(self):
        return self.nombre_p

