from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

def htmltest(request):
    dictionary = {
        'name': "My first blog!",
        'intro': "lorem stuff and stuff and more stuff how are you doing today?",
    }
    return render(request, 'index.html', dictionary)


def root(request):
    return redirect("/test")


def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')
    

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')


def create(request):
    return redirect("/")
    
    
    
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")
    
    
def edit(request, number):
    return HttpResponse (f"placeholder to edit blog {number}")
    
    
def destory(request):
    return redirect("/blogs")
    
    
def jsonresp(request):
    return JsonResponse({"response": "JSON response from jsonresp", "status": True}, "is this even correct?")