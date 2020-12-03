from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt



def root(request):
    return render(request, 'index.html')

def reg_process(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/')
        
    else:
        password = request.POST["password"]
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        User.objects.create(
            fname = request.POST["fname"],
            lname = request.POST["lname"],
            email = request.POST["email"],
            hashpw = hashed,
        )
        messages.success(request, "Successfully registered. Please login.")
        return redirect ('/')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for val in errors.values():
            messages.error(request, val)
        return redirect('/')

    user = User.objects.filter(email=request.POST['email']) 
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST["password"].encode(), logged_user.hashpw.encode()):
            request.session['user_id'] = logged_user.id
            return redirect('/success')
    else:
        messages.error(request, "Login failed. Try again.")
    return redirect('/')

def success(request):
    context = {
        "user" : User.objects.get(id = request.session['user_id'])
    }
    return render(request, "welcome.html", context)
    
def logout(request):
    request.session.flush()
    return redirect('/')

