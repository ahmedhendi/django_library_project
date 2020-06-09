
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from author.models import Author

# Create your models here.


class Book(models.Model):
    Published = 'PB'
    Withdrawn = 'WD'
    Draft = 'DF'

    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="author_book")
    title = models.CharField(max_length=50)
    desc = models.TextField(default='')
    img = models.ImageField(upload_to='book_image/',default='book_image/default.png')
    state_choices = [
        (Published,'Published'),
        (Withdrawn,'Withdrawn'),
        (Draft,'Draft')
    ]
    state = models.CharField(max_length=2,choices=state_choices,default= '')
    created_date = models.DateTimeField(default=timezone.now)


    def is_upperclass(self):
        return self.state 
    
    
    
    def __str__(self):
        return self.title


    
