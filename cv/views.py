from django.shortcuts import render
from .models import TietojaMinusta

def home(request):
    tietoa = TietojaMinusta.objects.first()
    return render(request, 'cv/home.html', {'tietoa': tietoa})
