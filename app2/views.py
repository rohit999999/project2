from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from app2.forms import *

def register(request):
    reg=False
    userform=UserForm()
    profileform=ProfileForm()
    if request.method=="POST" and request.FILES:
        userform=UserForm(request.POST)
        profileform=ProfileForm(request.POST,request.FILES)
        if userform.is_valid() and profileform.is_valid():
            user=userform.save(commit=False) 
            user.set_password(userform.cleaned_data['password'])
            user.save()
            profile=profileform.save(commit=False)
            profile.user=user
            profile.save()
            return HttpResponseRedirect(reverse('app3:user_login'))
    return render(request,'register.html',context={'userform':userform,'profileform':profileform,'reg':reg})