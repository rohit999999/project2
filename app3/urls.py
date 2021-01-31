from django.urls import path
app_name='app3'
from app3 import views

urlpatterns= [
    path('login2/',views.user_login,name='user_login')
]