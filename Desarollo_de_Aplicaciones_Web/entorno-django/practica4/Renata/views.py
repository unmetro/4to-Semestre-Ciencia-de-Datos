from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def IndexView(request):
    '''Pagina Principal'''
    return HttpResponse("Renata Practica")