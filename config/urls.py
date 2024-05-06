from django.contrib import admin
from django.urls import path, include
from .settings.base import STATIC_DIR, STATIC_URL
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('debugtools.urls')),

    ### api
    path('api/', include('account.urls')),
    path('api/', include('nutritioninformation.urls')),
    # path('api-auth/', include('rest_framework.urls')),

    path('api/', include('etcetera.urls')),
]

# wtf!!! ++++++ need static file location
urlpatterns += static(STATIC_URL, document_root=STATIC_DIR)
