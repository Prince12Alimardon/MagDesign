from django.db import models
from user.models import Author
from django.conf import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.ImageField(upload_to='images')
    news = models.ForeignKey('News', models.CASCADE, related_name='images')

    def __str__(self):
        return self.news.title

    @property
    def image_path(self):
        return f"{settings.SITE_URL}{self.name.url}"


class News(models.Model):
    title = models.CharField(max_length=212)
    text = models.TextField()
    category = models.ManyToManyField('Category', related_name='news')
    views = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(Author, models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    deleted_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
