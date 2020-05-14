from django.contrib import admin
from .models import Review, Comment, Movie
# Register your models here.


# 어드민 사이트에 등록해줘
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Comment)
