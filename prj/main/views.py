from django.shortcuts import render
from .models import Pecivo

def get_homepage(request):
    pecivos = Pecivo.objects.prefetch_related('pecivokategorie_set__kategorie').all()

    if request.GET.get("search"):
        search_term = request.GET.get("search")
        print("SEARCH", search_term)
        pecivos = Pecivo.objects.filter(jmeno__icontains=search_term)

    context = {
        "svatek": "Marek",
        "pecivos": pecivos
    }

    return render(request, "main/homepage.html", context)
