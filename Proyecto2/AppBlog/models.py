from django.db import models

# Create your models here.

class Blog(models.Model):
    nombre= models.CharField(max_length=40)
    comision= models.IntegerField()

class Publicable(models.Model):
    fecha_publicada= models.DateField()
    nombre= models.CharField(max_length=40)
    publicado= models.BooleanField()

class Lector(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()

class Escritor(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    email= models.EmailField()