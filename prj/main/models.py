from statistics import mode
from django.db import models

class Pecivo(models.Model):
    jmeno = models.CharField(max_length=50)
    popis = models.CharField(max_length=3000)
    cena = models.IntegerField(null=True, blank=True)
    kategorie = models.ForeignKey("Kategorie", max_length=50, on_delete=models.SET_NULL, null=True)
    obrazek_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.jmeno}"


class Kategorie(models.Model):
    jmeno = models.CharField(max_length=100)
    cislo_kategorie = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.jmeno
    
class Recept(models.Model):
    jmeno = models.CharField(max_length=50)
    recept = models.CharField(max_length=1000)
    kategorie = models.ForeignKey("Kategorie",max_length=50,on_delete=models.SET_NULL, null=True )

    def __str__(self):
        return f"{self.jmeno}"

class PecivoKategorie(models.Model):
    kategorie = models.ForeignKey("Kategorie",max_length=50,on_delete=models.SET_NULL, null=True )
    pecivo = models.ForeignKey("Pecivo",max_length=50,on_delete=models.SET_NULL, null=True )
    def __str__(self):
        return f"{self.kategorie}{self.pecivo}"

class Obrazek(models.Model):
    obrazek_url = models.URLField(max_length=500) 

    def __str__(self):
        return self.obrazek_url

