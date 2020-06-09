from django.conf.urls import url
from . import views

app_name = 'author'

urlpatterns = [
     
     url(r'^author$', views.index ,name="author"),
     url(r'^(?P<id>\d+)/author$', views.author_details ,name='author_details'),
]