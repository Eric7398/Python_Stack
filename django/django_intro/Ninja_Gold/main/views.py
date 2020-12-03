from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    request.session['counter'] = 0
    request.session['x'] = []
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index.html')


def farm(request):
    rng = random.randint(10,20)
    request.session['counter'] += rng
    (request.session['x']).append(f"Gold from Farm is {rng}")
    print("Gold from Farm is", rng)
    return redirect("/new")

def cave(request):
    rng = random.randint(5,10)
    request.session['counter'] += rng
    (request.session['x']).append(f"Gold from Cave is {rng}")
    print("Gold from Cave is", rng)
    return redirect("/new")

def house(request):
    rng = random.randint(2,5)
    request.session['counter'] += rng
    (request.session['x']).append(f"Gold from House is {rng}")
    print("Gold from House is", rng)
    return redirect("/new")

def casino(request):
    rng = random.randint(-50,50)
    request.session['counter'] += rng
    (request.session['x']).append(f"Gold from Casino is {rng}")
    print("Gold from Casino is", rng)
    return redirect("/new")

def delete(request):
    del request.session['counter']
    return redirect("/")