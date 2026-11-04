from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MessageForm
from .models import Actualite, Evenement, Photo


def accueil(request):
       actualites = Actualite.objects.order_by('-date')[:3]
       evenements = Evenement.objects.order_by('date')[:3]
       return render(request, 'blog/accueil.html', {
           'actualites': actualites,
           'evenements': evenements,
       })


def galerie(request):
       photos = Photo.objects.all()
       return render(request, 'blog/galerie.html', {'photos': photos})


def contact(request):
       if request.method == 'POST':
           form = MessageForm(request.POST)
           if form.is_valid():
               form.save()
               messages.success(request, "Merci, votre message a bien été envoyé.")
               return redirect('contact')
       else:
           form = MessageForm()
       return render(request, 'blog/contact.html', {'form': form})
def presentation(request):
       return render(request, 'blog/presentation.html')