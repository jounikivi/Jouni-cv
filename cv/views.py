from django.shortcuts import render
from .models import TietojaMinusta, Tyokokemus, Koulutus, Taidot


def home(request):
    tietoa = TietojaMinusta.objects.first()
    tyokokemukset = Tyokokemus.objects.all().order_by('-alkupvm')
    koulutukset = Koulutus.objects.all().order_by('-aloitusvuosi')
    taidot = Taidot.objects.all().order_by('-taso')

    context = {
        'tyokokemukset': tyokokemukset,
        'koulutukset': koulutukset,
        'taidot': taidot,
    }
    if tietoa is not None:
        context['tietoa'] = tietoa

    return render(request, 'cv/home.html', context)

