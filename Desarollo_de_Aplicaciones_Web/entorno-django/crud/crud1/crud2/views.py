from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .form import ProductoForm
from django.http import HttpResponse

def inicio(request):
    return render(request,'inicio.html')
    
def listar(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def detalles(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalles.html', {'producto': producto})

def crear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ProductoForm()
    return render(request, 'crear.html', {'form': form})

def borrar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar')
    return render(request, 'borrar.html', {'producto': producto})

def actualizar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'actualizar.html', {'form': form})
