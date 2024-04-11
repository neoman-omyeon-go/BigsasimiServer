from django.urls import path
from .views import *

urlpatterns = [
    path('get_ingestioninformation/', IngestionInformationAPI.as_view()),
]
