from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('app1:home'))
