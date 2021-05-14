from django.contrib import admin
from django.urls import path
from apps.setting import views

urlpatterns = [
    path('', views.index, name='setting'),
]
