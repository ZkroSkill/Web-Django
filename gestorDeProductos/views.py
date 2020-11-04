from gestorDeProductos.models import usuario
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def mantenedor(request):
    return render(request, 'mantenedor.html',{})

def galeria(request):
    return render(request, 'galeria.html',{})

def login(request):
    return render(request, 'login.html',{})

def registrar(request):
    mensaje = ""
    rut         = "No indentificado"
    email       = "No indentificado"
    contraseña  = "No indentificado"
    nombreC     = "No indentificado"
    fechaNac    = "No indentificado"
    telefono    = "No indentificado"
    if request.method == "POST":
        if 'btnGrabar' in request.POST:
            rut        = request.POST ["txtrut"]
            email      = request.POST ["txtemail"]
            contraseña = request.POST ["contraseña"]
            nombreC    = request.POST ["txtNombre"]
            fechaNac   = request.POST ["txtfechaNac"]
            telefono   = request.POST ["txttelefono"]
            usuario.objects.create(rut = rut,email = email, contraseña = contraseña,nombreC = nombreC, fechaNac = fechaNac, telefono = telefono)
            mensaje = "sirvio la wea"
    contexto = {"Paso lo siguiente:" : mensaje}
    return render(request, 'registrar.html', contexto)