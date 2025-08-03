from django.db import models

# Create your models here.
class TietojaMinusta(models.Model):
  otsikko = models.CharField(max_length=100)
  kuvaus = models.TextField()
  kuva = models.ImageField(upload_to='kuvat/')
  
  def __str__(self):
    return self.otsikko
  
  
class Tyokokemus(models.Model):
    yritys = models.CharField(max_length=100)
    tehtava = models.CharField(max_length=100)
    kuvaus = models.TextField()
    alkupvm = models.DateField()
    loppupvm = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.tehtava} at {self.yritys}"
    
class Koulutus(models.Model):
    oppilaitos = models.CharField(max_length=100)
    tutkinto = models.CharField(max_length=100)
    kuvaus = models.TextField()
    aloitusvuosi = models.DateField()
    valmistumisvuosi = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.tutkinto} at {self.oppilaitos}"

class Taidot(models.Model):
    taito = models.CharField(max_length=100)
    taso = models.IntegerField(choices=[(i, f"{i}/5") for i in range(1, 6)])

    def __str__(self):
        return f"{self.taito} {self.taso}"
