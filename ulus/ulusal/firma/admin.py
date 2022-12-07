from django.contrib import admin
from .models import Firma, FirmaCategory

# Register your models here.
admin.site.register(Firma)
admin.site.register(FirmaCategory)