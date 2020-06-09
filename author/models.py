from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    desc = models.TextField(default='')
    img = models.ImageField(upload_to='author_image/',default='author_image/default.png')

    def __str__(self):
        return self.name