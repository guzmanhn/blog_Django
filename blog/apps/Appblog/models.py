from django.db import models

# Create your models here.

class Entrada(models.Model):
	titulo = models.CharField(max_length=100)
	contenido = models.TextField()
	fecha = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.titulo

class comment(models.Model):
	fechacreacion = models.DateTimeField(auto_now_add=True)
	autor = models.CharField(max_length=100)
	mensaje = models.TextField()
	idEntrada = models.ForeignKey(Entrada)

	def __str__(self):
		return self.autor
