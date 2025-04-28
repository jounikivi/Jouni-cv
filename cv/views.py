from django.shortcuts import render
from .models import TietojaMinusta

def home(request):
    tietoja = TietojaMinusta.objects.all()
    return render(request, 'cv/home.html', {'tietoja': tietoja})
