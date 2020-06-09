from django.shortcuts import render ,get_object_or_404 , redirect

from books.models import Book
from .forms import bookform
# Create your views here.

def all_books(request):
    all_books = Book.objects.all()

    context = {
        'all_books' : all_books
    }
    return render(request, 'all_books.html',context)




def add_book(request):
        if request.method =='POST':
            form = bookform(request.POST)
            if form.is_valid():
                new_form =form.save(commit= False)
                new_form.user=request.user
                new_form.save()
                return redirect('/')


        else :
            form = bookform()


        context = {
            'form': form
        }

        return render(request,'add_book.html',context) 



def get_book(request,id):
    # current_post = post.objects.get(id = id)
    current_book = get_object_or_404(Book,id=id)

    context = {
        'book': current_book 
    }
    return render( request,'detail.html',context)





def edit_book(request,id):
    cur_book = get_object_or_404(Book,id=id)
    if request.method =='POST':
        form = bookform(request.POST, instance=cur_book )
        if form.is_valid():
            new_form =form.save(commit= False)
            new_form.user=request.user
            new_form.save()
            return redirect('/')

    else :
        form = bookform(instance=cur_book)


    context = {
        'form': form
    }

    return render(request,'edit_book.html',context) 

def admin(request):
    return redirect('admin')




def delete_book(request,id):
    cr_book = get_object_or_404(Book,id=id)
    cr_book.delete()
    return redirect("/")
