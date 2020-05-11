from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.photolist, name ='photolist'),
    path('community/', views.create, name ='create'),
]
