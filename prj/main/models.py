from django.db import models

class Pecivo(models.Model):
    jmeno = models.CharField(max_length=50)
    popis = models.CharField(max_length=3000)
    cena = models.FloatField(null=True, blank = True)
    kategorie = models.ForeignKey("Kategorie",max_length=50,on_delete=models.SET_NULL, null=True )

    def __str__(self):
        return f"{self.jmeno}"

class Kategorie(models.Model):
    jmeno = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.jmeno}"
    
