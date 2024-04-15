from django.urls import path
from .views import IngestionInformationAPI, IngestionInformationListAPI, DailyInformationAPI, IngestionInformationAllListAPI

urlpatterns = [
    path('get_ingestioninformation/', IngestionInformationAPI.as_view()),
    path('get_ingestioninformationList/', IngestionInformationListAPI.as_view()),
    path('get_ingestioninformationAllList/', IngestionInformationAllListAPI.as_view()),
    path('get_dailyinformation/', DailyInformationAPI.as_view()),
]
