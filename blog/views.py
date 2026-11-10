from django.shortcuts import render
from .models import Actualite
from .models import Actualite, Photo, Video
from django.shortcuts import render, get_object_or_404
from .models import Actualite, Photo, Video, Maire

def accueil(request):
    actualites = Actualite.objects.order_by('-date')[:5]
    maires = Maire.objects.all()
    return render(request, 'blog/accueil.html', {'actualites': actualites, 'maires': maires})

def maire_detail(request, pk):
    maire = get_object_or_404(Maire, pk=pk)
    return render(request, 'blog/maire.html', {'maire': maire})
def galerie(request):
    photos = Photo.objects.filter(categorie='village').order_by('-date')
    return render(request, 'blog/galerie.html', {'photos': photos})

def videos(request):
    videos = Video.objects.order_by('-date')
    return render(request, 'blog/videos.html', {'videos': videos})

def gamou(request):
    photos = Photo.objects.filter(categorie='gamou').order_by('-date')
    return render(request, 'blog/gamou.html', {'photos': photos})


def presentation(request):
    return render(request, 'blog/presentation.html')


def contact(request):
    return render(request, 'blog/contact.html')
