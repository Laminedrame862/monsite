from django.urls import path
from . import views

urlpatterns = [
path('', views.accueil, name='accueil'),
path('presentation/', views.presentation, name='presentation'),
path('galerie/', views.galerie, name='galerie'),
path('videos/', views.videos, name='videos'),
path('gamou/', views.gamou, name='le_gamou'),
path('contact/', views.contact, name='contact'),
path('maires/<int:pk>/', views.maire_detail, name='maire_detail'),  
]