from django.urls import path
from .views import UserAPI, SuscieAPI

urlpatterns = [
    path('users/', UserAPI.as_view()),
    path('sus/', SuscieAPI.as_view()),
]