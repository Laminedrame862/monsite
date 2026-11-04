from django.urls import path
from . import views

urlpatterns = [
       path('', views.accueil, name='accueil'),
       path('galerie/', views.galerie, name='galerie'),
       path('contact/', views.contact, name='contact'),
       path('presentation/', views.presentation, name='presentation'),
       ]