from django.http import HttpResponse
from .models import Persona, Articulo
from .forms import PersonaForm, LocalidadForm, CategoriaForm, Unidad_medidaForm, ArticuloForm, TipoMovimientoForm, MovimientoForm
from django.shortcuts import render, get_object_or_404, redirect

def index(request, template_name="index.html"):
    art_list = Articulo.objects.all()
    datos_art = {"art_list": art_list}
    return render(request, template_name, datos_art)

def acerca_de(request):
    return HttpResponse("Curso de Python y Django")
#lista de clientes
def clientes(request, template_name="entidad/clientes.html"):
     #trae todo los objetos que tiene la clase persona, esto reemplaza select * from persona
    cliente_list = Persona.objects.all()
     #la clave clientes es la que voy a usar en el html
    datos = {"clientes": cliente_list}
    return render(request, template_name, datos)
#funcion cargar clientes nuevos
def cargar_cliente(request, template_name="entidad/nuevo_cliente.html"):
    #si se valida el formulario se guarda
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('cliente')
    else:
        #si no es valido devuelve el formulario vacio
        form = PersonaForm
    datos = {"form": form}
    return render(request, template_name, datos)
#funcion editar algun cliente
def editar_cliente(request, pk, template_name="entidad/nuevo_cliente.html"):
    cliente=get_object_or_404(Persona, pk=pk)
    form = PersonaForm(request.POST or None, instance=cliente)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect("cliente")
        else:
            print(form.errors)
            return render(request, template_name, {"form": form})
    else:
        return render(request, template_name, {"form":form})

def borrar_cliente(request, pk, template_name="entidad/cliente_confirm_delete.html"):   
    cliente = get_object_or_404(Persona, pk=pk)
    #si el method = post es que se dio confirmar (submit) en el html y se activó POST
    if request.method == "POST":
        cliente.delete()
        return redirect("cliente")
    else:
        return render(request, template_name)

#funcion listar articulos 
def articulo(request, template_name="entidad/articulos.html"):
    art_list = Articulo.objects.all()
    datos = {"articulos": art_list}
    return render(request, template_name, datos)
#Funcion cargar articulos
def cargar_articulo(request, template_name="entidad/nuevo_articulo.html"):
    #si se valida el formulario se guarda
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("El articulo se ha cargado")
    else:
        #si no es valido devuelve el formulario vacio
        form = ArticuloForm
    datos = {"form": form}
    return render(request, template_name, datos)
#funcion para editar algun articulo
def editar_articulo(request, pk, template_name="entidad/nuevo_articulo.html"):
    articulo=get_object_or_404(Articulo, pk=pk)
    form = ArticuloForm(request.POST or None, instance=articulo)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect("articulos")
        else:
            print(form.errors)
            return render(request, template_name, {"form": form})
    else:
        return render(request, template_name, {"form":form})    
#funcion borrar articulos
def borrar_articulo(request, pk, template_name="entidad/articulo_confirm_delete.html"):
    articulo = get_object_or_404(Articulo, pk=pk)
    if request.method == "POST":
        articulo.delete()
        return redirect("articulo")
    else:
        return render(request, template_name)     

#Funcion listar categoria
def categoria(request, template_name="entidad/categorias.html"):
    cat_list = CategoriaForm()
    datos = {"categorias": cat_list}
    return render(request, template_name, datos)
#Funcion cargar categoria nueva
def cargar_categoria(request, template_name="entidad/nueva_categoria.html"):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("La categoria se ha cargado")
    else:
        #si no es valido devuelve el formulario vacio
        form = CategoriaForm
    datos = {"form": form}
    return render(request, template_name, datos)
#Funcion editar categoria
def editar_categoria(request, pk, template_name="entidad/nueva_categoria.html"):
    categoria=get_object_or_404(Articulo, pk=pk)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect("categoria")
        else:
            print(form.errors)
            return render(request, template_name, {"form": form})
    else:
        return render(request, template_name, {"form":form})
#Funcion borrar categoria
def borrar_categoria(request, pk, template_name="entidad/categoria_confirm_delete.html"):
    categoria = get_object_or_404(categoria, pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect("categoria")
    else:
        return render(request, template_name)

#Funcion mostrar contactos 
def show_contact(request, template_name="entidad/contacto.html"):
    return render(request, template_name)