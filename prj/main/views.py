from django.shortcuts import render
from .models import Pecivo, Kategorie

def get_homepage(request):
    pecivos = Pecivo.objects.select_related('kategorie').all()
    kategorie = Kategorie.objects.all()

    if request.GET.get("search"):
        search_term = request.GET.get("search")
        pecivos = pecivos.filter(jmeno__icontains=search_term)

    if request.GET.get("category"):
        category_id = request.GET.get("category")
        pecivos = pecivos.filter(kategorie__id=category_id)

    context = {
        "svatek": "Marek",
        "pecivos": pecivos,
        "kategorie": kategorie,
    }

    return render(request, "main/homepage.html", context)
