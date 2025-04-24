from django.db import models

# Create your models here.
class TietojaMinusta(models.Model):
  otsikko = models.CharField(max_length=100)
  kuvaus = models.TextField()
  kuva = models.ImageField(upload_to='kuvat/')
  
  
class Tyokokemus(models.Model):
    yritys = models.CharField(max_length=100)
    tehtava = models.CharField(max_length=100)
    kuvaus = models.TextField()
    alkupvm = models.DateField()
    loppupvm = models.DateField()
    
class Koulutus(models.Model):
    oppilaitos = models.CharField(max_length=100)
    tutkinto = models.CharField(max_length=100)
    kuvaus = models.TextField()
    aloitusvuosi = models.DateField()
    valmistumisvuosi = models.DateField()

class Taidot(models.Model):
    taido = models.CharField(max_length=100)
    taso = models.CharField(max_length=100)