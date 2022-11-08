
from django.contrib import admin
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/', views.detail, name='detail'),
    
    
]
