from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
     
     url(r'^$', views.all_books ,name="all_books"),
     url(r'^add$', views.add_book ,name='add_book'),
     url(r'^(?P<id>\d+)$', views.get_book ,name='book'),
     url(r'^(?P<id>\d+)/edit$', views.edit_book ,name='edit_book'),
    url(r'^admin$', views.admin ,name='admin'),    
     url(r'^(?P<id>\d+)/delete$', views.delete_book ,name='delete_book'),
     url(r'^$', views.home ,name='home'),


]