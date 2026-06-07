from django.shortcuts import render,redirect
from .models import Book,Author 
def index(request):
    context={
        'all_books':Book.objects.all(),
    }
    return render(request,'index.html',context)
    
def create_book(request):
    if request.method == 'POST' :
        Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
        )
        return redirect('/')
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    available_authors = Author.objects.exclude(books=book)
    context={
        'book':book,
        'available_authors':available_authors,
    }
    return render(request,'book_detail.html',context)
def add_author_to_book(request,book_id):
    if request.method=='POST':
        book=Book.objects.get(id=book_id)
        author=Author.objects.get(id=request.POST['author_id'])
        book.authors.add(author)
    return redirect(f'/books/{book_id}')
def authors(request):
    context={
        'all_authors':Author.objects.all(),
    }
    return render(request,'authors.html',context)
def create_author(request):
    if request.method=='POST':
        Author.objects.create(
            first_name = request.POST['first_name'],
            last_name  = request.POST['last_name'],

        )
        return redirect('/authors')
def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    available_books = Book.objects.exclude(authors=author)
    context = {
        'author': author,
        'available_books': available_books,
    }
    return render(request, 'author_detail.html', context)

def add_book_to_author(request, author_id):
    if request.method == 'POST':
        author = Author.objects.get(id=author_id)
        book   = Book.objects.get(id=request.POST['book_id'])
        author.books.add(book)
    return redirect(f'/authors/{author_id}')