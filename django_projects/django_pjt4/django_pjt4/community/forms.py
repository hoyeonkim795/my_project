from django import forms
from .models import Review, Movie
from .models import Comment

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_title', 'poster', 'rank', 'content']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rank','image','content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
