from django.db import models

class Pecivo(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=False,null=True)
