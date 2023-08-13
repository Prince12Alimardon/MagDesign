from django.urls import path, include


urlpatterns = [
    path('news/', include('news.urls')),
    path('user/', include('user.urls')),
]