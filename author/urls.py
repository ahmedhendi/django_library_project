from django.conf.urls import url
from . import views

app_name = 'author'

urlpatterns = [
     
     url(r'^addauthor$', views.add_author ,name="author"),
     url(r'^(?P<id>\d+)/author$', views.author_details ,name='author_details'),
     url(r'^authors$', views.all_authors ,name="all_author"),
     url(r'^(?P<id>\d+)/books$', views.all_author_books ,name="all_author_books"),
]
