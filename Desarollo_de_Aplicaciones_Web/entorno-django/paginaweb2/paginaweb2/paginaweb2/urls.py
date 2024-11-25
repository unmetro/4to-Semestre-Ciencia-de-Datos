"""
URL configuration for paginaweb2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pagina_web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base, name='base'),
    path('about/', views.about, name='about'),
    path('mona/', views.mona, name='mona'),
    path('luna/', views.luna, name='luna'),
    path('blade',views.blade, name='blade'),
    path('mob/', views.mob, name='mob'),
    path('frieren/', views.frieren, name='frieren'), 
    
]
