from django.shortcuts import render, HttpResponse, redirect
from login_reg_app.models import User
from .models import *

def index(request):
    context = {
        "myuser" : User.objects.get(id = request.session['user_id']),
        "book": Book.objects.all(),
        "firstreview": Review.objects.all().order_by('-id')[:3],
        "otherreview": Review.objects.all().order_by('-id')[3:],
    }
    return render(request, "books.html", context)

def addbook(request):
    context = {
        "author": Author.objects.all()
    }
    return render(request, "booksadd.html", context)

def addproc(request):
    newbook = Book.objects.create(
        title = request.POST['title']
    )
    
    id = newbook.id
    
    
    Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        forbook = Book.objects.get(id = id),
        byuser = User.objects.get(id = request.session['user_id']),
    )
    
    
    
    
    if len(request.POST['existauthor']) > 0:
        addauthor = request.POST['existauthor']
    else:
        addauthor = Author.objects.create(
            name = request.POST['author']
        )
    
    newbook.authors.add(addauthor)

    return redirect(f"/books/{id}")



def addreview(request, id):
    Review.objects.create(
        review = request.POST['review'],
        rating = request.POST['rating'],
        forbook = Book.objects.get(id = id),
        byuser = User.objects.get(id = request.session['user_id']),
    )
    return redirect(f"/books/{id}")

def booksinfo(request, id):
    context = {
        "book": Book.objects.get(id=id),
        "person": User.objects.get(id=request.session["user_id"])
    }
    return render(request, "booksinfo.html", context)

def deletereview(request, id):
    d = Review.objects.get(id=id)
    d.delete()
    id = request.POST['return']
    return redirect(f'/books/{id}')


def userinfo(request, id):
    user = User.objects.get(id = id)
    unique = []
    for review in user.byusers.all():
        if review.forbook not in unique:
            unique.append(review.forbook)
    
    context = {
        "user": User.objects.get(id = id),
        "unique": unique,
    }
    
    return render(request, "user.html", context)