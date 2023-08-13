from django.urls import path
from .views import NewsAPI, NewsDetailAPI, CategoryAPI


urlpatterns = [
    path('category/', CategoryAPI.as_view()),
    path('news/', NewsAPI.as_view()),
    path('news-detail/<int:pk>/', NewsDetailAPI.as_view()),
]