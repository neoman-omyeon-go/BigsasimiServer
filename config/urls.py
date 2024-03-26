from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('debugtools.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# wtf!!!
# if settings.DEBUG is False:
#     urlpatterns += [
#         re_path(r'^{{static/}}/(?P<path>.*)$', serve, {'document_root': settings.STATIC_DIR}),
#     ]