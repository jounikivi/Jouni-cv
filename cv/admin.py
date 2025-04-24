from django.contrib import admin
from .models import TietojaMinusta, Tyokokemus, Koulutus, Taidot

# Register your models here.
admin.site.register(TietojaMinusta)
admin.site.register(Tyokokemus)
admin.site.register(Koulutus)
admin.site.register(Taidot) 