from django.db import models

class TblColegio(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    contacto = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class TblZona(models.Model):
    colegio = models.ForeignKey(TblColegio, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    