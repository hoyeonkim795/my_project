from django import forms
from .models import Review
from .models import Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'movie_title', 'rank', 'image','content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
