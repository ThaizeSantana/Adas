from django.urls import path
from app_website import views


urlpatterns = [
    path('', views.index),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('filmes/', views.filmes),
    path('estrelas/', views.estrelas),
    path('insecure/', views.insecure),
    path('kakegurui/', views.kakegurui),
    path('irmaes/', views.irmaes),
    
]