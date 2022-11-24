"""Proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import mostrar_blog, mostrar_index, crear_blog, crear_escritor,registrar_lector,buscar_blog

urlpatterns = [
    path('mostrar_blog/', mostrar_blog),
    path('',mostrar_index),
    path('crear_blog/',crear_blog, name='Crear Blog'),
    path('crear_escritor/',crear_escritor, name='Crear Escritor'),
    path('registrar_lector/', registrar_lector, name='Registrar Lector'),
    path('buscar_blog/', buscar_blog, name='Buscar Blog'),
]
