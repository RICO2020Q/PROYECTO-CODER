from django.shortcuts import render
from .models import Blog, Lector, Escritor
from .forms import CrearEscritorForm, RegistrarLectorForm, CrearBlogForm
from django.http import HttpResponse

# Create your views here.

def mostrar_blog(request):
    blog=Blog(nombre='Python', comision='34635')

    saludo= f'Hola a todos, este es el blog de {blog.nombre}, con numero de comision: {blog.comision}'
    
    return HttpResponse(saludo)


def mostrar_index(request):

    return render(request, 'index.html')


def crear_escritor(request):

    
    if request.method == 'POST':
        
        formulario=CrearEscritorForm(request.POST)

        if formulario.is_valid():

            formulario_limpio=formulario.cleaned_data
            
            escritor= Escritor(nombre=formulario_limpio['nombre'], apellido=formulario_limpio ['apellido'],
            email=formulario_limpio ['email'])

            escritor.save()

            return render(request, 'index.html')
    
    else:
        formulario= CrearEscritorForm()
    return render(request,'crear_escritor.html', {'formulario': CrearEscritorForm} )

def registrar_lector(request):

    
    if request.method == 'POST':
        
        formulario=RegistrarLectorForm(request.POST)

        if formulario.is_valid():

            formulario_limpio=formulario.cleaned_data
            
            lector= Lector(nombre=formulario_limpio['nombre'], apellido=formulario_limpio ['apellido'],
            email=formulario_limpio ['email'])

            lector.save()

            return render(request, 'index.html')
    
    else:
        formulario= RegistrarLectorForm()
    return render(request,'registrar_lector.html', {'formulario': RegistrarLectorForm} )

def crear_blog(request):

    
    if request.method == 'POST':
        
        formulario=CrearBlogForm(request.POST)

        if formulario.is_valid():

            formulario_limpio=formulario.cleaned_data
            
            blog= Blog(nombre=formulario_limpio['nombre'], comision=formulario_limpio['comision'])

            blog.save()

            return render(request, 'index.html')
    
    else:
        formulario= CrearBlogForm()
    return render(request,'crear_blog.html', {'formulario': CrearBlogForm} )


def buscar_blog(request):

    if request.GET.get('comision',False):
        comision= request.GET['comision']
        blogs =Blog.objects.filter(comision__icontains=comision)

        return render(request,'buscar_blog.html',{'blogs':blogs})

    else:
        respuesta='No hay datos'
    
    return render(request,'buscar_blog.html',{'respuesta':respuesta})