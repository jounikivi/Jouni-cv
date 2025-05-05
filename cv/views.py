from django.shortcuts import render
from .models import TietojaMinusta, Tyokokemus


def home(request):
    tietoa = TietojaMinusta.objects.first()
    tyokokemukset = Tyokokemus.objects.all().order_by('-alkupvm')
    return render(request, 'cv/home.html', {
        'tietoa': tietoa,
        'tyokokemukset': tyokokemukset
    })

