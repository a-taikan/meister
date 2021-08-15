from django.urls import path
from . import views
from django.contrib import admin
from django.views.generic import base
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.showall, name= 'showall'),
    path('home/<int:article_id>/', views.blog_show)
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
