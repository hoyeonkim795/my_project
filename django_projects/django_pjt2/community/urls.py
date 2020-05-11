from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.review_list, name ='review_list'),
    path('create/',views.create, name='create'),
    path('<int:pk>/',views.review_detail, name='review_detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
