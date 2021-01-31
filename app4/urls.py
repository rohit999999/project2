from django.urls import path
app_name='app4'
from app4 import views

urlpatterns= [
    path('logout2/',views.user_logout,name='user_logout'),
]