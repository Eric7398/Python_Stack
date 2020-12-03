from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import TVshow, Network


def home(request):
    return redirect("/shows")

def main(request):
    context = {
		"tvshows" : TVshow.objects.all(),
    }
    return render(request, "main.html", context)



def showinfopage(request, id):
    context = {
        "tvshow" : TVshow.objects.get(id=id),
        "tvshow_list" : TVshow.objects.all()
    }
    return render(request, "showinfo.html", context)


def editpage(request, id):
    context = {
        "tvshow" : TVshow.objects.get(id=id),
        "tvshow_list" : TVshow.objects.all()
    }
    return render(request, "editpage.html", context)



def editpageprocess(request, id):
    errors = TVshow.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        
        return redirect(f'/shows/{id}/edit')
    
    
    else:
        theshow = TVshow.objects.get(id=id)
        theshow.title = request.POST["title"]
        theshow.network = request.POST["network"]
        theshow.release = request.POST["date"]
        theshow.desc = request.POST["desc"]
        theshow.save()
    
        return redirect(f'/shows/{id}')


def addpage(request):
    context = {
		"network_list" : Network.objects.all()
    }
    return render(request, 'newshow.html', context)

def addpageprocess(request):
    
    errors = TVshow.objects.basic_validator(request.POST)
    
    if len(errors) > 0:
        for k,v in errors.items():
            messages.error(request, v)
        
        return redirect('/shows/new')
    
    title = request.POST["title"]
    release = request.POST["date"]
    desc = request.POST["desc"]
    new_show = TVshow.objects.create(title = title, release = release, desc = desc)
    id = new_show.id
    
    nw = Network.objects.get(id=request.POST["network"])
    
    new_show.networks.add(nw)
    return redirect(f'/shows/{id}')


def index(request, id):
    d = TVshow.objects.get(id = id)
    d.delete()
    
    return redirect("/shows")