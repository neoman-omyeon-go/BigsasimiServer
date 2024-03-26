from django.contrib import admin
from django.urls import path, include, re_path
from .settings.base import STATIC_DIR, STATIC_URL
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('debugtools.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# wtf!!! ++++++ need static file location
urlpatterns += static(STATIC_URL, document_root=STATIC_DIR)