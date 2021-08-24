from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import base
from blog.views import Index



urlpatterns = [
    path('', views.home, name= 'home'),
    path('<int:article_id>/', views.blog_show, name= 'show'),
    path('post', Index.as_view(), name='post'),
]
