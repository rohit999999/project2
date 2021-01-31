from django.urls import path
app_name='app1'
from app1 import views

urlpatterns= [
    path('home2/',views.home,name='home'),
]