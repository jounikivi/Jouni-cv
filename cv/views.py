from django.shortcuts import render

def etusivu(request):
    return render(request, 'cv/etusivu.html', {})
