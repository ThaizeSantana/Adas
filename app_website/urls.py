from django.urls import path
from app_website import views


urlpatterns = [
    path('', views.index),
    
]