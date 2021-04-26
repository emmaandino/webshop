from django.contrib import admin
from entidad import models

my_models = [models.Persona, models.Localidad, models.Categoria, models.Articulo, models.Pais, models.Movimiento]

admin.site.register(my_models)

# Register your models here.
