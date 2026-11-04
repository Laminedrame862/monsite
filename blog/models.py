from django.db import models

# Create your models here.
from django.db import models


class Actualite(models.Model):
       titre = models.CharField(max_length=200)
       contenu = models.TextField()
       image = models.ImageField(upload_to='actualites/', blank=True)
       date = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return self.titre


class Evenement(models.Model):
       nom = models.CharField(max_length=200)
       lieu = models.CharField(max_length=200)
       date = models.DateField()
       description = models.TextField(blank=True)

       def __str__(self):
           return self.nom


class Photo(models.Model):
       legende = models.CharField(max_length=200)
       image = models.ImageField(upload_to='galerie/')

       def __str__(self):
           return self.legende


class Message(models.Model):
       nom = models.CharField(max_length=100)
       email = models.EmailField()
       texte = models.TextField()
       date = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return f"{self.nom} - {self.email}"