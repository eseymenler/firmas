from django.urls import path
from . import views
from .views import  firmaana, firmadetail, firmacategory

urlpatterns = [
    

    path("", views.firmaana, name="firma-frontpage"),
    path("<slug:slug>/", views.firmadetail, name="firma-detail"),
    path("kategory/<slug:slug>/", views.firmacategory, name="firma-category"),
   
]