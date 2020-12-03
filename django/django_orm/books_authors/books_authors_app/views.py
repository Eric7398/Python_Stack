from django.shortcuts import render, redirect
from .models import Book, Author


def index(request):
    context = {
        "books" : Book.objects.all(),
    }
    
    return render(request, "index.html", context)


def authors(request):
    context = {
        "authors" : Author.objects.all(),
    }
    return render(request, "author.html", context)


def add_to_list(request):
	if request.POST["which_form"] == "book":
		Book.objects.create(
			title = request.POST["title"],
			desc = request.POST["desc"],
		)
	else:
		Author.objects.create(
        first_name = request.POST["fname"],
        last_name = request.POST["lname"],
        notes = request.POST["notes"],
    )
	return redirect('/')


def book_info(request, id):
    context = {
		"this_book" : Book.objects.get(id=id),
		"authors" : Author.objects.all(),
	}
    return render(request, "disp_books.html", context)


def author_info(request, id):
    context = {
        "this_author" : Author.objects.get(id=id),
		"books" : Book.objects.all(),
    }
    return render(request, "disp_authors.html", context)


def add_to_author_page(request, id):
    book_to_add = Book.objects.get(id=request.POST["book_list"])
    Author.objects.get(id=id).books.add(book_to_add)
    return redirect(f'/authors/{id}')


def add_to_book_page(request, id):
    author_to_add = Author.objects.get(id=request.POST["author_list"])
    Book.objects.get(id=id).authors.add(author_to_add)
    return redirect(f'/books/{id}')