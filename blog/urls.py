from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import base



urlpatterns = [
    path('', views.showall, name= 'showall'),
    path('<int:article_id>/', views.blog_show)
]
