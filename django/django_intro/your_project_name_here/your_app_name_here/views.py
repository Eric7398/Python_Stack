from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("some string")


def test(request):
    dictionary = {
        'name': "hello",
        "num": 123,
    }
    return render(request, 'index.html', dictionary)


def hey(request,aname):
    return HttpResponse(f'{aname} AND THE NAME WORKS!')

def redirected_to_home(request):
    return redirect('/')