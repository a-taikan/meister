from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
