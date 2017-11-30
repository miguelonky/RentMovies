from django.contrib import admin
from . models import movies
from . models import rentmovie

# Register your models here.
admin.site.register(movies)
admin.site.register(rentmovie)
