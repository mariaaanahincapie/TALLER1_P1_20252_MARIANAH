from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('agregar/', views.add_movie, name='add_movie'),
    path('about/', views.about, name='about'),
]
