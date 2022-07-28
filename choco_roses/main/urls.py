from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('', views.main, name='main-url')
]