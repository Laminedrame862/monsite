from django.contrib import admin
from .models import Actualite, Photo, Video
from .models import Actualite, Photo, Video, Maire

admin.site.register(Maire)
admin.site.register(Actualite)
admin.site.register(Photo)
admin.site.register(Video)
def __str__(self):
    return self.nom