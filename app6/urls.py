from django.urls import path
app_name='app6'
from app6 import views

urlpatterns= [
    path('changepass2/',views.change_password,name='change_password'),
]