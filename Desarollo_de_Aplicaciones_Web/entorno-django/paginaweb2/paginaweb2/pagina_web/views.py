from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def blade(request):
    return render(request, 'blade.html')

def mona(request):
    return render(request, 'mona.html')

def luna(request):
    return render(request, 'luna.html')

def mob(request):
    return render(request, 'mob.html')

def frieren(request):
    return render(request, 'frieren.html')

def index(request):
    return render(request, 'index.html')