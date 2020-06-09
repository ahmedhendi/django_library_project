from django.shortcuts import render ,get_object_or_404 , redirect
from author.models import Author

from django.http import HttpResponse
# Create your views here.


def index (request):
    return render(request,'author.html')

def author_details (request,id):
    current_author = get_object_or_404(Author,id=id)

    context = {'author': current_author }
    return render( request,'author_details.html',context)
    