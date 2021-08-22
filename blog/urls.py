from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import base



urlpatterns = [
    path('', views.home, name= 'home'),
    path('<int:article_id>/', views.blog_show, name= 'show'),
]
