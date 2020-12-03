from django.shortcuts import render, HttpResponse, redirect
from .models import User
			#importing "User" from data

def index(request):
    context = {
        "allusers": User.objects.all()
    }
    return render(request, "index.html", context)


def info(request):
	# this is basically User.objects.all()
    user = User()
    #info from data becomes info from html (server?)
    user.first_name = request.POST.get('first_name')
    user.last_name = request.POST.get('last_name')
    user.email = request.POST.get('email')
    user.age = request.POST.get('age')
    user.save()
    return redirect('/')



def delete(request):
    d = User.objects.last()
    d.delete()
    return redirect('/')
