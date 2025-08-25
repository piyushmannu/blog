from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *

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
    pass

