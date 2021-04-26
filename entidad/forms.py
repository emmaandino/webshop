from django.forms import ModelForm, DateInput
from django import forms
from .models import Persona
from .models import Localidad
from .models import Categoria
from .models import Unidad_medida
from .models import Articulo
from .models import TipoMovimiento
from .models import Movimiento

class DateInput(forms.DateInput):
    input_type = 'date'

#los formularios estan asociados a los models
class PersonaForm(ModelForm):
    #inicializador de la clase
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Ingrese el nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Ingrese el apellido'}),
            'edad': forms.TextInput(attrs={'type': 'number', 'size': 2, 'class': 'form-control w-100', 'placeholder': 'Ingrese la edad'}),
             #se hizo la clase dateinput para que fecha de nacimiento tenga el tipo date como dato ingresado             
            'fecha_nac': DateInput(format='%y-%m-%d', attrs={'class': 'form-control w-100'}),
            'calle': forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Ingrese la calle'}),
            'localidad': forms.Select(attrs={'class': 'form-control w-100'}),
            'email': forms.TextInput(attrs={'class': 'form-control w-100', 'placeholder': 'Ingrese el email'}),
            'activo': forms.CheckboxInput(),
            'fecha_carga': forms.DateInput(attrs={'class': 'form-control w-100'}),
            'fecha_actualizacion': forms.DateInput(attrs={'class': 'form-control w-100'}),
        }


class LocalidadForm(ModelForm):
    class Meta:
        model = Localidad
        fields = '__all__'
        widgets = {
            'nombre_l': forms.TextInput(),
            'cp': forms.TextInput(attrs={'type': 'number', 'size': 4}),
            'provincia': forms.TextInput(),
            'fecha_carga': forms.HiddenInput(),
            'fecha_actualizacion': forms.HiddenInput(),
        }


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(),
            'descripcion': forms.TextInput(),
        }

class Unidad_medidaForm(ModelForm):
    class Meta:
        model = Unidad_medida
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(),
            'formula': forms.TextInput(),
            'fecha_carga': forms.HiddenInput(),
            'fecha_actualizacion': forms.HiddenInput(),
        }


class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ('codigo','nombre','descripcion', 'cantidad', 'unidad_de_medida', 'precio', 'descuento', 'aumento','iva','flete','ganancia','imagen')
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'number'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'descripcion': forms.TextInput(),
            'cantidad': forms.TextInput(attrs={'type': 'number'}),
            'unidad_de_medida': forms.TextInput(attrs={'type': 'number'}),
            'precio': forms.TextInput(attrs={'type': 'number'}),
            'precio_lista': forms.TextInput(attrs={'type': 'number'}),
            'descuento': forms.TextInput(attrs={'type': 'number'}),
            'aumento': forms.TextInput(attrs={'type': 'number'}),
            'iva': forms.TextInput(attrs={'type': 'number'}),
            'flete': forms.TextInput(attrs={'type': 'number'}),
            'ganancia': forms.TextInput(attrs={'type': 'number'}),
            }


class TipoMovimientoForm(ModelForm):
    class Meta:
        model = TipoMovimiento
        fields = '__all__'
        widgets = {
            'nombre_tp': forms.TextInput(),
            'abreviatura': forms.TextInput(),
            'autonumerico': forms.BooleanField(),
            'fecha_carga': forms.HiddenInput(),
            'fecha_actualizacion': forms.HiddenInput(),
        }


class MovimientoForm(ModelForm):
    class Meta:  
        model = Movimiento
        fields = '__all__'
        widgets = {
            'tipo': forms.TextInput(),
            'fecha': forms.HiddenInput(),
            'numero': forms.TextInput(attrs={'type': 'number'}),
            'cliente': forms.TextInput(),
            'subtotal': forms.TextInput(attrs={'type': 'number'}),
            'total': forms.TextInput(attrs={'type': 'number'}),
            'articulo': forms.TextInput(),
            'cantidad': forms.TextInput(attrs={'type': 'number'}),
            'fecha_carga': forms.HiddenInput(),
            'fecha_actualizacion': forms.HiddenInput(),
        }
