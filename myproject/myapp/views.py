from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Feature,Services,Team
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
    
def app(request):
    features = Feature.objects.all()
    services = Services.objects.all()
    teams = Team.objects.all()
    
    return render (request, 'app.html', {'features':features, 'services':services , 'teams':teams})

def register(request):
    if request.method == 'POST':
        username=request.POST['Username']
        email=request.POST['Email']
        password=request.POST['Password']
        password2=request.POST['Password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('register')
            
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate (username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('app')
        else:
            messages.info(request, "You are not Registered to this website") 
            return redirect('register')  
        
    return render(request,'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('app')


    