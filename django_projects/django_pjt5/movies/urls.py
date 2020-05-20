from django.urls import path
from . import views


app_name = 'movies'


urlpatterns = [
    path('', views.movie_list, name = 'movie_list'),
    path('create/', views.movie_create, name= 'movie_create'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('<int:pk>', views.movie_detail, name='movie_detail'),
    path('recommend/', views.movie_recommend, name='movie_recommend'),

]
