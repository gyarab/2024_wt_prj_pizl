from django.contrib import admin
from .models import Pecivo, Kategorie, Recept, PecivoKategorie


class PecivoAdmin(admin.ModelAdmin):
    list_display = ["jmeno","popis","cena", "kategorie"]

class KategorieAdmin(admin.ModelAdmin):
    list_display = ["jmeno"]

class ReceptAdmin(admin.ModelAdmin):
    list_display = ["jmeno","recept","kategorie"]

class PecivoKategorieAdmin(admin.ModelAdmin):
    list_display = ["kategorie","pecivo"]


admin.site.register(Pecivo, PecivoAdmin)
admin.site.register(Kategorie, KategorieAdmin)
admin.site.register(Recept, ReceptAdmin)
admin.site.register(PecivoKategorie, PecivoKategorieAdmin)
