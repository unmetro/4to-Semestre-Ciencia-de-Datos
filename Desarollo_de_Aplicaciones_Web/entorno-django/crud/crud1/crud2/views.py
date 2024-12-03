from django.shortcuts import render

# Create your views here.
def listar(request):
    return render(request, 'listar.html')

def detalles(request):
    return render(request, 'detalles.html')

def crear(request):
    return render(request, 'crear.html')

def borrar(request):
    return render(request, 'borrar.html')

def actualizar(request):
    return render(request, 'actualizar.html')