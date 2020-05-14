from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.movie_list, name = 'movie_list'),
    path('create/', views.movie_create, name= 'movie_create'),
    path('review/', views.review_list, name ='review_list'),
    path('<int:movie_pk>/review_create/',views.review_create, name='review_create'),
    path('<int:pk>/review',views.review_detail, name='review_detail'),
    path('<int:pk>/review_update/', views.review_update, name='review_update'),
    path('<int:pk>/review_delete/', views.review_delete, name='review_delete'),
    path('<int:review_pk>/comments/', views.comments_create, name="comments_create"),
    path('<int:review_pk>/comments/<int:comment_pk>/delete', views.comments_delete, name="comments_delete"),
    path('<int:review_pk>/review_like/', views.review_like, name='review_like'),
    path('<int:pk>', views.movie_detail, name='movie_detail'),
    path('<int:review_pk>like/', views.like, name='like'),
    path('<int:pk>/movie_update/', views.movie_update, name='movie_update'),
    path('<int:pk>/movie_delete/', views.movie_delete, name='movie_delete'),
]
