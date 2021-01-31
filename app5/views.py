from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app2.forms import *

# Create your views here.
@login_required
def profile_info(request):
    username=request.session.get('username')
    user=User.objects.get(username=username)
    profile=Profile.objects.get(user=user)
    return render(request,'profile_info.html',context={'user':user,'profile':profile})