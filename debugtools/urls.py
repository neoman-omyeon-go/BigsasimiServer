from django.urls import path
from .views import test_index
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('test/', test_index.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
