from django import forms
from .models import Publicacion, Seccion

#choices = [('tecnologos', 'lifestyle', 'arte y cultura', 'viajes')]
choices = Seccion.objects.all().values_list('name')
choices_list = []

for item in choices:
	choices_list.append(item)

class PublicacionForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		fields = ('titulo', 'seccion', 'autor', 'publicacionImage', 'descripcion', 'contenido', 'snippet')

		widget = {
			'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'escribe el titulo de tu historia'}),
			'seccion': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
			'autor': forms.TextInput(attrs={'class': 'form-control', 'id': 'elder', 'type': 'hidden'}),
			'publicacionImage': forms.FileInput(attrs={'class': 'form-control'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'contenido': forms.Textarea(attrs={'class': 'form-control'}),
			'snippet': forms.Textarea(attrs={'class': 'form-control'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Publicacion
		fields = ('titulo', 'descripcion', 'contenido')

		widget = {
			'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'escribe el titulo de tu historia'}),
			'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
			'contenido': forms.Textarea(attrs={'class': 'form-control'}),
		}