from django.contrib import admin
from django.urls import path, include  
from app import views

urlpatterns = [
    path('', views.Homeview, name='home'),
    path('list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.post_search, name='post_search'),
   
]
