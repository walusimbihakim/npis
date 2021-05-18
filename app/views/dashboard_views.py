from django.conf.urls import url
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def index_page_view(request):
    return render(request, "login.html")

@login_required(login_url="login")
def index_page(request):
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if request.GET.get('next',None):
                return redirect(request.GET['next'])
            return redirect('index_page')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    
    else:
        return render (request,'login.html')  

def logout(request):
    auth.logout(request)
    return redirect('/')
