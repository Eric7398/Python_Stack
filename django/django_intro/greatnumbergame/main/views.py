from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    
    if 'message' not in request.session: 
        request.session['message'] = ""
        
    print("-------------------------------------------------------")
    print(request.session['number'])
    return render(request, "index.html")



def delete(request):
    del request.session['number']
    del request.session['message']
    return redirect('/')



def rng(request):
    
    theory = int(request.POST.get('guess'))
    if theory < request.session['number']:
        request.session['message'] = "Too low!"
        print ("Too low")
    
    elif theory > request.session['number']:
        request.session['message'] = "Too high"
        print ("Too high")
        
    else:
        theory == request.session['number']
        request.session['message'] = "Correct"

    return redirect('/')

    
    
    
    
    
    
    
    
    


    
