from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("upload/", views.Home, name='Home'),
]