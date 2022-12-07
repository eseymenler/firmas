from django.urls import path
from . import views
from .views import frontpage, detail, category

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("<slug:slug>/", views.detail, name="detail"),
    path("kategory/<slug:slug>/", views.category, name="category"),

    
   
]
