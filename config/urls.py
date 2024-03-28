from django.contrib import admin
from django.urls import path, include
from .settings.base import STATIC_DIR, STATIC_URL
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('debugtools.urls')),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# wtf!!! ++++++ need static file location
urlpatterns += static(STATIC_URL, document_root=STATIC_DIR)