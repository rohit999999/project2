from django.urls import path
app_name='app5'
from app5 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    path('prof2/',views.profile_info,name='profile_info'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)