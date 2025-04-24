from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)


class Diagnosis(models.Model):
    injuries = models.CharField(max_length=500)
    pastinjuries = models.CharField(max_length=500)

class Record(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)  # Un usuario puede tener varios registros
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)  # Un diagnóstico puede estar en varios registros
    injuries = models.TextField()  # Copia de las injuries del Diagnosis
    pastinjuries = models.TextField()  # Copia de las pastinjuries del Diagnosis
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro