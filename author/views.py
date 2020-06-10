from django.shortcuts import render ,get_object_or_404 , redirect
from .models import Author
from .forms import authorform
from django.http import HttpResponse
from books.models import Book
from books import views

# Create your views here.



def add_author(request):
        if request.method =='POST':
            form = authorform(request.POST)
            if form.is_valid():
                new_form =form.save(commit= False)
                new_form.user=request.user
                new_form.save()
                return redirect('/')


        else :
            form = authorform()


        context = {
            'form': form
        }

        return render(request,'author.html',context) 

def author_details (request,id):
    current_author = get_object_or_404(Author,id=id)

    context = {'author': current_author }
    return render( request,'author_details.html',context)
    



def all_authors(request):
    all_authors = Author.objects.all()
    
    context = {
        'all_authors' : all_authors
    }
    return render(request, 'all_author.html',context)


def all_author_books(request,id):
    all_author_books =Book.objects.filter(author__id=id)
    context = {
        'all_author_books' : all_author_books
    }
    return render(request, 'all_author_books.html',context)