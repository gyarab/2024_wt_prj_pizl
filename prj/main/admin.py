from django.contrib import admin
from .models import Pecivo

class PecivoAdmin(admin.ModelAdmin):
    list_display = ["jmeno","popis","cena"]

admin.site.register(Pecivo, PecivoAdmin)