from django.urls import path
from .views import UserRegister, UserLogin, UserLogout, UserProfileAPI
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    ### 계정
    path('signup/', UserRegister.as_view()),
    path('login/', UserLogin.as_view()),
    path('logout/', UserLogout.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),    # post : 발급
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # post : 만료된 토큰 재발급

    ### 프로필
    path('profile/', UserProfileAPI.as_view(), name='user_profile_api'),   # 프로필 조회
]
