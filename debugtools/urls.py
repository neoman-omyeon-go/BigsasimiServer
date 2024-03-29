from django.urls import path
from .views import test_index, test_detail, test_JWT_authentication, test_open_view
from rest_framework.urlpatterns import format_suffix_patterns

# test url
urlpatterns = [
    path('', test_index.as_view()),
    path('<int:pk>/', test_detail.as_view()),
    path('authonly/', test_JWT_authentication.as_view()),
    path('test_open_view/', test_open_view.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
