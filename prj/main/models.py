from django.db import models

class Pecivo(models.Model):
    jmeno = models.CharField(max_length=50)
    popis = models.CharField(max_length=300)
    cena = models.IntegerField(null=True, blank = True)

    def __str__(self):
        return f"{self.name}"
