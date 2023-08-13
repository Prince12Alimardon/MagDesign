from rest_framework import generics
from .models import Author, Suscie
from .serializer import UserSerial, SuscieSerializer


class UserAPI(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = UserSerial


class SuscieAPI(generics.CreateAPIView):
    queryset = Suscie.objects.all()
    serializer_class = SuscieSerializer
