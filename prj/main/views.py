from django.shortcuts import render
from .models import Pecivo

def get_homepage(request):
    context = {
        "svatek": "Marek",
        "pecivo": Pecivo.objects.all().order_by('jmeno') [:10]
    }

    print("HOST",request.get_host())
    
    if(request.GET.get("search")):
        print("SEARCH",request.GET.get("search"))
        pecivo = pecivo.filtet(title__contains=request.GET.get("search"))


    return render(
        request, "main/homepage.html", context
        )