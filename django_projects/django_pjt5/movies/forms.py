from django import forms
from .models import Genre, Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ['genre', 'like_users']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'