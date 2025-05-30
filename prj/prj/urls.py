from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from main.views import get_homepage, pecivo_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_homepage, name='homepage'),
    path('homepage/', TemplateView.as_view(template_name='main/homepage.html')),
    path('pecivo/<int:pk>/', pecivo_detail, name='pecivo_detail'),
    path('recepty/', TemplateView.as_view(template_name='main/recepty.html')),
]
