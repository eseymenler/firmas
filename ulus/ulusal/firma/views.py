from django.shortcuts import render
from .models import Firma, FirmaCategory

# Create your views here.
def firmaana(request):
    firmalar = Firma.objects.all()

    context = {
        'firmalar': firmalar

    }


    return render(request, 'firma/firma-frontpage.html', context)


def firmadetail(request, slug):
    firmax = Firma.objects.get(slug=slug)

    context = {
        'firmax': firmax

    }  

    return render(request, 'firma/firma-detail.html', context)


def firmacategory(request, slug):
    firmacategory = FirmaCategory.objects.get(slug=slug)

    context = {
        'firmacategory': firmacategory

    }  

    return render(request, 'firma/firma-category.html', context)