from django.contrib import admin
from .models import Movie, Genre

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'popularity', 'vote_count', 'vote_average']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)