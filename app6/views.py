from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from app2.forms import *

# Create your views here.
@login_required
def change_password(request):
    username=request.session['username']
    if request.method=="POST":
        password=request.POST.get('password')
        user=User.objects.get(username=username)
        user.set_password(password)
        user.save()
        return HttpResponseRedirect(reverse('app3:user_login'))
    return render(request,'change_password.html')
