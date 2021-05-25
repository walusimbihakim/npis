from django.conf.urls import url
from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import REDIRECT_FIELD_NAME, login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

from app.decorators.decorator import field_required

def index_page_view(request):
    return render(request, "login.html")

# @login_required(login_url="login")


# @method_decorator([login_required, field_required], name='dispatch')
# @login_required(login_url="login")
# @field_required()
def index_page(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return render(request, 'login.html')
   

    

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
