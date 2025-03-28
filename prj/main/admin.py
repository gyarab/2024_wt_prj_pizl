from django.contrib import admin
from .models import Pecivo, Kategorie


class PecivoAdmin(admin.ModelAdmin):
    list_display = ["jmeno","popis","cena", "kategorie"]

class KategorieAdmin(admin.ModelAdmin):
    list_display = ["jmeno"]


admin.site.register(Pecivo, PecivoAdmin)
admin.site.register(Kategorie, KategorieAdmin)