from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.urls import reverse

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user and user.is_active:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect(reverse('app1:home'))
        else:
            return HttpResponse('Enter correct username and password')
    return render(request,'user_login.html')
