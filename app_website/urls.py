from django.urls import path
from app_website import views


urlpatterns = [
    path('', views.index),
    path('cadastro/', views.cadastro),
    path('login/', views.login),
    path('filmes/', views.filmes),
]