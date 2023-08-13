from django.conf import settings
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=212)
    profession = models.CharField(max_length=212)
    icon = models.FileField(upload_to='author_image', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def icon_path(self):
        return f"{settings.SITE_URL}{self.icon.url}"


class Suscie(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
