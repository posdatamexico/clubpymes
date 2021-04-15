from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Seccion(models.Model):
	name = models.CharField(max_length=200, default="")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')

class Publicacion(models.Model):
	titulo = models.CharField(max_length=200)
	seccion = models.CharField(max_length=100, default="")
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	publicacionImage = models.ImageField(null=True)
	descripcion = models.CharField(max_length=200)
	contenido = RichTextField(blank=True, null=True)
	fecha = models.DateField(auto_now_add=True)
	snippet = models.CharField(max_length=255, default='Da click en el enlace para leer la historia completa')
	likes = models.ManyToManyField(User, related_name="pub")

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.titulo 

	def get_absolute_url(self):
		return reverse('home')

