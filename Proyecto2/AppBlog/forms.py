from django import forms

class CrearBlogForm(forms.Form):
    nombre= forms.CharField(max_length=40)
    comision= forms.IntegerField()

class RegistrarLectorForm(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()

class CrearEscritorForm(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido= forms.CharField(max_length=40)
    email= forms.EmailField()





