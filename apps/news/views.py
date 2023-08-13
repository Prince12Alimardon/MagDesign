from rest_framework import generics
from .serializer import NewsSerial, NewsdetailSerial, CategorySerial, ImageSerial
from .models import Category, News, Image


class CategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerial


class NewsAPI(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerial

    def get_queryset(self):
        ab = self.queryset.all()
        is_view = self.request.query_params.get('is_view')
        cat = self.request.query_params.get('cat')
        if is_view:
            ab = ab.filter(views__isnull=False)
        if cat:
            ab = ab.filter(category__name__exact=cat)
        return ab


class NewsDetailAPI(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsdetailSerial


