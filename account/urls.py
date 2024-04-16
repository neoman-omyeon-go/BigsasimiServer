from django.urls import path
from .views import UserRegister, UserLogin, UserLogout, UserProfileAPI, UserProfileAddAPI, UserProfileRemoveAPI
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
    path('profile_add/', UserProfileAddAPI.as_view(), name='user_profile_add_api'),   # 프로필 수정(리스트 추가)
    path('profile_remove/', UserProfileRemoveAPI.as_view(), name='user_profile_remove_api'),   # 프로필 수정(리스트 삭제)
]
