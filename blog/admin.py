from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Actualite, Evenement, Photo, Message

admin.site.register(Actualite)
admin.site.register(Evenement)
admin.site.register(Photo)
admin.site.register(Message)