from django.db import models
import datetime

# Create your models here.

#Comments model
class Comment(models.Model):
    nickname = models.CharField(max_length = 20)
    comment = models.CharField(max_length = 300)
    date = models.DateField(auto_now = True)

#ExperienciaLaboral model
class ExperienciaLaboral(models.Model):
    titulo = models.CharField(max_length = 30)
    empresa = models.CharField(max_length = 50)
    descripcion = models.CharField(max_length = 300)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

#Project model
class Project(models.Model):
    titulo = models.CharField(max_length = 30)
    repository_link = models.URLField()
    descripcion = models.CharField(max_length = 300)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

#Skill model
class Skill(models.Model):
    technology = models.CharField(max_length = 30)
    expertise_level = models.PositiveSmallIntegerField()

#Leadership model
class Leadership(models.Model):
    date = models.DateField()
    descripcion = models.CharField(max_length = 300)
