
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.Downloader, name='home'),
]
