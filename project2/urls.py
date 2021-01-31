"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import app1
import app2
import app3
import app4
import app5
import app6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1/',include('app1.urls')),
    path('reg1/',include('app2.urls')),
    path('login1/',include('app3.urls')),
    path('logout1/',include('app4.urls')),
    path('prof1/',include('app5.urls')),
    path('changepass1/',include('app6.urls')),
]
