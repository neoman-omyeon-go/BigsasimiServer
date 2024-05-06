from django.urls import path
from .views import SearchList

urlpatterns = [
    # 검색
    path('get_search_list/', SearchList.as_view(), name='get_search_list'),
]
