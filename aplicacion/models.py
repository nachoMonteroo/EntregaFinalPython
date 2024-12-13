from django.db import models

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    ano = models.IntegerField()
    division = models.CharField(max_length=1)
    inasistencias = models.DecimalField(max_digits=3,decimal_places=1)
    fecha_de_nacimiento=models.DateField()
    email=models.EmailField()

    def __str__(self):
        return self.nombre + " " +  self.apellido

    

class Profesores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    inasistencias = models.DecimalField(max_digits=2,decimal_places=1)
    fecha_de_nacimiento=models.DateField()
    email=models.EmailField()

    def __str__(self):
        return self.nombre + " " +  self.apellido

class Directivo(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre + " " +  self.apellido