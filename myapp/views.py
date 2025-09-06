from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate

# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = usercreation(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User created")
    else:
        form = usercreation()
    return render(request,'create.html',{'form':form})

def login_user(request):
    show_data = User.objects.all()
    return render(request,'show.html',{'data':show_data})

def authenticate(request):
    if request.method == 'POST':
        usernname = request.POST.get('username')
        password = request.POST.get('password')
        user = User.authenticate(request,username = usernname,password = password)
        if user is not None:
            return HttpResponse("Login Success")
        else:
            return HttpResponse("Login Failed")
    return render(request,'login.html')
