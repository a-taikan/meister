from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import base




urlpatterns = [
    path('', views.home, name= 'home'),
    path('<int:article_id>/', views.blog_show, name= 'show'),
    path('post', views.FormView.as_view() ,name="post"),
    path('<int:article_id>/add_img', views.add_img, name="add_img"),
    path('search', views.search, name= 'search'),
    path('category/<str:category>', views.category_choise, name='category' )
]
