from django.urls import path
from .views import UserRegister, UserLogin, UserLogout
from django.conf.urls import include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('signup/', UserRegister.as_view()),
    path('login/', UserLogin.as_view()),
    path('logout/', UserLogout.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # post : 발급
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # post : 만료된 토큰 재발급
]