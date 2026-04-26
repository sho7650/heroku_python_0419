"""herokuwebinar URL Configuration

See https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path

from helloworld import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
